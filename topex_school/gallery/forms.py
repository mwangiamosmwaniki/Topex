from django import forms
from .models import Photo

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['album', 'image', 'caption']
        widgets = {
            'album': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
        }
