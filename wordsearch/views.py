from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(req):
    return render(req, 'wordsearch/index.html')

def resultsPageView(req, search_word):
    context = {'search_word': search_word}
    return render(req, 'wordsearch/results.html', context)
