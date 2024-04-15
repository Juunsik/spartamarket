from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Products
from .forms import ProductForm

# Create your views here.
def product_list(request):
    products=Products.objects.all()
    context={'products':products}
    return render(request, 'products/product_list.html', context)

@login_required
def product_create(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            product=form.save(commit=False)
            product.author=request.user
            product.save()
            return redirect('products:list')
    else:
        form=ProductForm()
    
    context={'form':form}
    return render(request, 'products/product_create.html', context)


def product_detail(request, pk):
    product=get_object_or_404(Products, pk=pk)
    context={'product':product}
    return render(request, 'products/product_detail.html', context)


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass


def product_wish(request, pk):
    pass


def product_hits(request, pk):
    pass