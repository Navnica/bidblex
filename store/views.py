from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Product
from django.contrib.staticfiles import finders


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


def product(request, pk):
    return render(request, 'store/product.html', {'product': get_object_or_404(Product, pk=pk)})


def img(request, filename):
    file_path = finders.find(f'store/img/{filename}')
    return FileResponse(open(file_path, 'rb'))


def docs(request, filename):
    file_path = finders.find(f'store/docs/{filename}')
    return FileResponse(open(file_path, 'rb'))
