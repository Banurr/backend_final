from django import forms
from .models import Category

class MediaFileForm(forms.ModelForm):
    class Meta:
        model =Category
        fields = ('name', 'image')