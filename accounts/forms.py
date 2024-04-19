from django.contrib.auth.forms import UserCreationForm
from django.forms import ClearableFileInput, TextInput, PasswordInput, CharField
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=UserCreationForm.Meta.fields+('image',)
        
        widgets={
            'username': TextInput(attrs={'placeholder':'username', 'class':"form-control form-control-lg"}),
            'image': ClearableFileInput(attrs={'class':'form-control'}),
        }
        
    password1=CharField(widget=PasswordInput(attrs={'placeholder':'password', 'class':'form-control'}))
    password2=CharField(widget=PasswordInput(attrs={'placeholder':'password confirm', 'class':'form-control'}))