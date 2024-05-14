from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


def product(request, pk):
    return render(request, 'store/product.html', {'product': get_object_or_404(Product, pk=pk)})


def img(request, filename):
    return FileResponse(open(f'store/static/img/{filename}', 'rb'))


def docs(request, filename):
    return FileResponse(open(f'store/static/docs/{filename}', 'rb'))


def login(request):
    return render(request, 'store/login.html')

