from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    get_user_model,
)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .forms import CustomUserCreationForm
from products.models import Product


# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:profile", user.username)
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('products:list')
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("products:list")


def delete(request):
    pass


def update(request):
    pass


def change_password(request):
    pass


@login_required
def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    products=Product.objects.filter(author=member.pk)
    wishs=Product.objects.filter(wish=request.user)

    context = {
        "member": member,
        'products':products,
        'wishs':wishs,
    }
    return render(request, "accounts/profile.html", context)


@login_required
@require_POST
def follow(request, pk):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=pk)
        if member != request.user:
            if member.follow.filter(pk=request.user.pk).exists():
                member.follow.remove(request.user)
            else:
                member.follow.add(request.user)
        return redirect("accounts:profile", username=member.username)
    return redirect("accounts:login")
