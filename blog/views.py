from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def main(request):
    products = Product.objects.all()
    return render(request, 'blog/index.html', {'products': products})

def about(request):
    return render(request, 'blog/about.html')
