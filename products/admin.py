from django.contrib import admin
from .models import Product, Offer # import the Product class from the models.py file


class ProductAdmin(admin.ModelAdmin): # ProductAdmin is a class that inherits from admin.ModelAdmin
    list_display = ('name', 'price', 'stock') #tuple of fields to display in the admin interface


admin.site.register(Product, ProductAdmin) # Admin object, site is attibute and object itself, 
                             # calling register method with argument Product. 
                             # This will make the Product model available in the admin interface.   

                             # We added ProductAdmin class as a second argument
                             # when registering the Product model, 
                             # wdjango will use the information in ProductAdmin class 
                             # to know how to represent a list of products.
                             # This will customize the way the Product model is displayed
                             # in the admin interface.

class OfferAdmin(admin.ModelAdmin): ## OfferAdmin is a class that inherits from admin.ModelAdmin
    list_display = ('code', 'discount') #tuple of fields to display in the admin interface

admin.site.register(Offer, OfferAdmin) # Admin object, site is attibute and object itself,
