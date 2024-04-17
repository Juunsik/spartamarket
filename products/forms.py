from django.forms import ModelForm, Textarea 
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        exclude=('author','wish','hits',)
        
        widgets={
            'description': Textarea(attrs={'cols':50,'rows':20})
        }