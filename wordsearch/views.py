from os import error
from django.shortcuts import render
from django.http import HttpResponse
from .api.urbandict import urbanDict
from .api.dictionaryapi import dictionaryAPI
from .models import *
from datetime import datetime

# Create your views here.
def indexPageView(request):
    return render(request, 'wordsearch/index.html')

def searchPageView(request):
    # get word from request
    search_word = str(request.GET['search_word']).lower().strip()

    # add to Database
    word = Search()
    word.search_word = search_word
    word.datetime_searched = datetime.now()
    word.save()

    # get the urban Dictionary Definition
    urban = urbanDict(search_word)
    if urban == error:
        urban = 'No definition Found'
    # get the diciontary Definition
    dictionary = dictionaryAPI(search_word)
    if dictionary == error:
        dictionary = 'No definition found'

    # set context
    context = {
        'search_word': search_word,
        'dictionary': dictionary,
        'urban': urban 
        }
    return render(request, 'wordsearch/search.html', context)
