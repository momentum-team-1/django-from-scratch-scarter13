from django import forms
from .models import Snippet 

class SnippetForm(forms.ModelForm):
    tag_names = forms.CharField(label="Tags", help_text="Enter tags seperated by spaces.")

    class Meta:
        model = Snippet
        fields = [
            'title',
            'description', 
            'text',
            'visibility',
        ]
        