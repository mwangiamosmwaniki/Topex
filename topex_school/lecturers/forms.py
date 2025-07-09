from django import forms
from academics.models import LectureNote, Assignment

class LectureNoteForm(forms.ModelForm):
    class Meta:
        model = LectureNote
        fields = ['unit', 'title', 'file', 'week', 'topic']
        widgets = {
            'unit': forms.Select(attrs={'class': 'form-input w-full'}),
            'title': forms.TextInput(attrs={'class': 'form-input w-full'}),
            'file': forms.FileInput(attrs={'class': 'form-input w-full'}),
            'week': forms.NumberInput(attrs={'class': 'form-input w-full'}),
            'topic': forms.TextInput(attrs={'class': 'form-input w-full'}),
        }



class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['unit', 'title', 'description', 'file', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
