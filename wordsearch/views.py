from django.shortcuts import render
from django.http import HttpResponse
from .urbandict import urbanDict

# Create your views here.
def indexPageView(request):
    return render(request, 'wordsearch/index.html')

def searchPageView(request):
    search_word = request.GET['search_word'].lower()
    definition = urbanDict(search_word)
    context = {
        'search_word': search_word,
        'definition': definition
        }
    return render(request, 'wordsearch/search.html', context)
