from django.db import models
from datetime import datetime

# Create your models here.
class Search(models.Model):
    search_word = models.CharField(max_length=50)
    datetime_searched = models.DateTimeField()

    def __str__(self):
        return (self.search_word)
    
    @property
    def getSearchWord(self):
        return (self.search_word)   