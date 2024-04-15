from django.shortcuts import render
from .models import Products

# Create your views here.
def product_list(request):
    products=Products.objects.all()
    context={'products':products}
    return render(request, 'products/product_list.html', context)


def product_create(request):
    pass


def product_detail(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass


def product_wish(request, pk):
    pass


def product_hits(request, pk):
    pass