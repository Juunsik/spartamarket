from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods, require_POST
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
            next_url=request.GET.get('next') or 'index' # 메인 페이지: 추후 생성 예정
            return redirect(next_url)
    else:
        form=AuthenticationForm()
    context={'form':form}
    return render('request', 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('index') # 메인 페이지: 추후 생성 예정


def delete(request):
    pass


def update(request):
    pass


def change_password(request):
    pass


def profile(request, username):
    pass

