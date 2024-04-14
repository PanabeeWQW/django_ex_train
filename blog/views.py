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
    products = Product.objects.all()

    # Получение параметра сортировки из GET-запроса
    sort_by = request.GET.get('sort_by')

    # Сортировка товаров в зависимости от параметра сортировки
    if sort_by == 'newest':
        products = products.order_by('-production_year')
    elif sort_by == 'oldest':
        products = products.order_by('production_year')
    elif sort_by == 'name':
        products = products.order_by('name')
    elif sort_by == 'price-':
        products = products.order_by('-price')
    elif sort_by == 'price+':
        products = products.order_by('price')
    else:
        # Если параметр сортировки не указан или некорректен, выводим товары без сортировки
        pass

    if cat_id is not None:
        category = Category.objects.get(pk=cat_id)
        products = products.filter(category=category)
    else:
        category = None

    return render(request, 'blog/catalog.html', {'category': category, 'products': products, 'cats': cats})


def category(request, cat_id):
    cats = Category.objects.all()
    category = Category.objects.get(pk=cat_id)
    products = Product.objects.filter(category=category)

    # Получение параметра сортировки из GET-запроса
    sort_by = request.GET.get('sort_by')

    # Сортировка товаров в зависимости от параметра сортировки
    if sort_by == 'newest':
        products = products.order_by('-production_year')
    elif sort_by == 'oldest':
        products = products.order_by('production_year')
    elif sort_by == 'name':
        products = products.order_by('name')
    elif sort_by == 'price-':
        products = products.order_by('-price')
    elif sort_by == 'price+':
        products = products.order_by('price')
    else:
        # Если параметр сортировки не указан или некорректен, выводим товары без сортировки
        pass

    return render(request, 'blog/catalog.html', {'category': category, 'products': products, 'cats': cats})
