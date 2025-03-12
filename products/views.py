from django.shortcuts import render
from django.http import HttpResponse


"""
All views fuction always take parameter request object.
Because when we go to a link, http sents a request, 
this function takes this request object as an parameter.
"""
def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Products')


# Note:
# In this file, we created two views.
# First view is index view. When user go to the root directory of products app,
# this view will be shown.
# Second view is new view. When user go to the new directory of products app,
# this view will be shown.

