from django import forms
from .models import Blog
class blogform(forms.ModelForm):
    class Meta:
        model =Blog
        fields=['name','email']