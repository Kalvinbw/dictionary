from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('search/', searchPageView, name='search')
]