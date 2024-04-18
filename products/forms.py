from django.forms import ModelForm, Textarea, TextInput, NumberInput, ClearableFileInput
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        exclude=('author','wish','hits',)
        
        widgets={
            'title': TextInput(attrs={'placeholder':'Title', 'class':"form-control form-control-lg"}),
            'description': Textarea(attrs={'placeholder':'Description', 'class':"form-control"}),
            'price': NumberInput(attrs={'placeholder':'Price', 'class':"form-control"}),
            'image': ClearableFileInput(attrs={'class':'form-control'}),
        }