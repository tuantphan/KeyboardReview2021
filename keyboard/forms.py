from django import forms
from .models import KeyboardName, KeyboardReview, KeyboardType

class KeyboardForm(forms.ModelForm):
    class Meta:
        model=KeyboardName
        fields='__all__'

class KeyboardImageForm(forms.ModelForm):
    class Meta:
        model=KeyboardReview
        fields='__all__'