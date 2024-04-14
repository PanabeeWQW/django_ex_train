from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def main(request):
    products = Product.objects.all()
    return render(request, 'blog/index.html', {'products': products})

def about(request):
    products = Product.objects.all()
    return render(request, 'blog/about.html', {'products': products})

def findus(request):
    return render(request, 'blog/findus.html')

def product(request, product_id):
    product = Product.objects.get(pk=product_id)  # Получаем объект товара по его идентификатору
    return render(request, 'blog/product.html', {'product': product})

def catalog(request, cat_id=None):
    cats = Category.objects.all()
    if cat_id is not None:
        category = Category.objects.get(pk=cat_id)
        products = Product.objects.filter(category=category)
    else:
        category = None
        products = Product.objects.all()
    return render(request, 'blog/catalog.html', {'category': category, 'products': products, 'cats': cats})

def category(request, cat_id):
    all_products = Product.objects.all()
    category = Category.objects.get(pk=cat_id)
    products = Product.objects.filter(category=category)
    cats = Category.objects.all()
    return render(request, 'blog/catalog.html', {'all_products': all_products, 'products': products, 'category': category, 'cats': cats})
