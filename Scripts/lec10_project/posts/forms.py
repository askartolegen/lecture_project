from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields ="__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.Textarea(attrs={'cols': 60, 'rows': 18})
        }


