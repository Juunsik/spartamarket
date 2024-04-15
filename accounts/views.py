from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm

# Create your views here.
@require_http_methods(['GET','POST'])
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

@require_http_methods(['GET','POST'])
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url=request.GET.get('next') or 'index'
            return redirect(next_url)
    else:
        form=AuthenticationForm()
    context={'form':form}
    return render('request', 'accounts/login.html', context)


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

