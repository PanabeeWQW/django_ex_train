from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('about/', about, name='about'),
    path('find_us/', findus, name='find_us'),
    path('product/<int:product_id>/', product, name='product'),
    path('category/<int:cat_id>/', category, name='category'),
    path('catalog/', catalog, name='catalog'),
]
