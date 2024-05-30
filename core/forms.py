from django import forms
from .models import NewsLetter

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['name', 'email']
