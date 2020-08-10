from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Restaurants(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=500)
    dirName = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=1000,unique=True)
    mapUrl = models.CharField(max_length=10000,unique=True)
    imgUrl = ArrayField(models.CharField(max_length=50, blank=True))
    
    
    
    
