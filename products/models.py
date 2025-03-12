from django.db import models


class Product(models.Model): # Product is a class that inherits from models.Model
    name = models.CharField(max_length=255) #attributes of the class
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

