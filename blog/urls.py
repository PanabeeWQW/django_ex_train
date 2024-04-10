from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('about/', about, name='about'),
    path('find_us/', findus, name='find_us'),
]
