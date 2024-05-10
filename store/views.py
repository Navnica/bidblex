from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


def product(request, pk):
    return render(request, 'store/product.html', {'product': get_object_or_404(Product, pk=pk)})