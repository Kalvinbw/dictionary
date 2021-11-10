from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(req):
    return render(req, 'wordsearch/index.html')