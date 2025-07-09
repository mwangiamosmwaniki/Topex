from django import forms
from .models import Applicant, Application, Course

class ApplicationForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if Applicant.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
