from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import render

class candidate(models.Model):
    name=models.CharField(max_length=100)
    logo=models.CharField(max_length=100)
    political_party=models.CharField(max_length=100)
    quote=models.CharField(max_length=500)
    photo=models.CharField(max_length=1000)
    area=models.CharField(max_length=100,default="Amritsar central")

    def get_absolute_url(self):
      return reverse('voting:index')

    def __str__(self):
        return self.name+' - '+self.political_party