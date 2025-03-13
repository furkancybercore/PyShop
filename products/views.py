from django.shortcuts import render
from django.http import HttpResponse
from .models import Product # Importing Product model from models.py file.



"""
All views fuction always take parameter request object.
Because when we go to a link, http sents a request, 
this function takes this request object as an parameter.
and return whatever we want.
"""
def index(request):
    products = Product.objects.all() # Fetch all products from database and load them to products variable.
    #return HttpResponse('Products Homepage')
    return render(request, 'index.html',
                  {'products': products})

'''
   How render function works:
        Render function takes request object as a first argument. 
        
        Second arguemnt is the name of template.
        django will look for this template in the templates directory of the app.
        In this case, it will look for index.html in products/templates directory.
        And render this template to the user.

        Third argument is the context. Context is a dictionary 
        that contains all the data that we want to pass to the template.
        In this case, we are passing products to the template.
        So, we can use this products variable in the template.
        We can use this products variable to show all products in the template.
'''

def new(request):
    return HttpResponse('New Products')


# Note:
# In this file, we created two views.
# First view is index view. When user go to the root directory of products app,
# this view will be shown.
# Second view is new view. When user go to the new directory of products app,
# this view will be shown.

