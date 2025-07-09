from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['phone', 'address', 'emergency_contact_name', 'emergency_contact_phone', 'semester']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),  # ✅ New widget
        }

