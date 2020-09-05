from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Restaurants(models.Model):
    
    restaurant_name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 300)
    
class FOOD(models.Model):

    restaurants = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    food_name = models.CharField(max_length = 100)
    price = models.IntegerField()

class Profit(models.Model):

    restaurants = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    daily = models.IntegerField()
    weekly = models.IntegerField()
    monthly = models.IntegerField()
