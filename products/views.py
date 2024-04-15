from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_list(request):
    products=Product.objects.all()
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
    product=get_object_or_404(Product, pk=pk)
    context={'product':product}
    return render(request, 'products/product_detail.html', context)

@login_required
def product_update(request, pk):
    product=get_object_or_404(Product, pk=pk)
    if product.author==request.user:
        if request.method=='POST':
            form=ProductForm(request.POST, instance=product)
            if form.is_valid():
                product=form.save()
                return redirect('products:detail', product.pk)
        else:
            form=ProductForm(instance=product)
            context={
                'form':form,
                'product':product,
                }
            return render(request, 'products/product_update.html', context)
    else:
        return redirect('products:list') 

@login_required
def product_delete(request, pk):
    product=get_object_or_404(Product, pk=pk)
    if request.user.is_authenticated:
        if product.author==request.user:
            product.delete()
    return redirect('products:list')


def product_wish(request, pk):
    pass


def product_hits(request, pk):
    pass