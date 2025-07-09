from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from django import forms

# Custom form to handle Profile creation with id_number and password
class ProfileAdminForm(forms.ModelForm):
    id_number = forms.CharField(help_text="e.g. P100/1681gG/21")
    password = forms.CharField(widget=forms.PasswordInput, help_text="Temporary password for the user", required=False)

    class Meta:
        model = Profile
        fields = ['id_number', 'role', 'bio', 'password']

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ('id_number', 'role', 'user')

    def save_model(self, request, obj, form, change):
        if not change:
            id_number = form.cleaned_data['id_number']
            password = form.cleaned_data.get('password') or User.objects.make_random_password()
            username = id_number.replace('/', '_')  # Sanitize ID to be a valid Django username

            # Create associated User
            user = User.objects.create_user(username=username, password=password)
            obj.user = user

        obj.save()

admin.site.register(Profile, ProfileAdmin)
