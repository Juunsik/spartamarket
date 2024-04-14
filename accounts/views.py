from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request, user)
            return redirect('profile')
    else:
        form=CustomUserCreationForm()
    context={'form':form}
    return render(request, 'accounts/signup.html', context)        


def login(request):
    pass


def logout(request):
    pass


def delete(request):
    pass


def update(request):
    pass


def change_password(request):
    pass


def profile(request, username):
    pass

