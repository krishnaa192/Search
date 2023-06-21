from django.db import models

# Create your models here.
from django.db import models

class Dish(models.Model):
    resturant_name = models.CharField(max_length=100)
    food=models.CharField(max_length=100)
