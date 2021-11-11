from django.shortcuts import render
from django.http import HttpResponse
from .urbandict import urbanDict
from .models import *
from datetime import datetime

# Create your views here.
def indexPageView(request):
    return render(request, 'wordsearch/index.html')

def searchPageView(request):
    search_word = request.GET['search_word'].lower()

    word = Search()
    word.search_word = search_word
    word.datetime_searched = datetime.now()
    word.save()

    definition = urbanDict(search_word)
    context = {
        'search_word': search_word,
        'definition': definition
        }
    return render(request, 'wordsearch/search.html', context)
