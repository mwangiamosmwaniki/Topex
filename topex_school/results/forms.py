from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'
        widgets = {
            'score': forms.NumberInput(attrs={'step': 0.01}),
            'grade': forms.TextInput(attrs={'maxlength': 2}),
            'semester': forms.Select(choices=[('Sem 1', 'Semester 1'), ('Sem 2', 'Semester 2')]),
        }
