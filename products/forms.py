from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        exclude=('author','wish','hits',)
        