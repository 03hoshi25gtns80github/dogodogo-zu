# forms.py
from django import forms
from .models import Upload

class MusicForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('description', 'document','music_url')
