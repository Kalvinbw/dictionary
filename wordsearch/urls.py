from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('<str:search_word>/', resultsPageView, name='results')
]