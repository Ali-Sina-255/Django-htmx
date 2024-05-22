from django import forms
from . models import Film

class ImageForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['film','photo']


