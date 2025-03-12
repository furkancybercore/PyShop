from django.shortcuts import render
from django.http import HttpResponse


"""
All views fuction always take parameter request object.
Because when we go to a link, http sents a request, 
this function takes this request object as an parameter.
"""
def index(request):
    return HttpResponse('Hello World')

