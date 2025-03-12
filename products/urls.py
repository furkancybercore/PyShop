from django.urls import path
from . import views # we imported views from the same directory


'''
we created this list oblect to keep our urls
'''
urlpatterns = [
    path('', views.index), # this is the path to the index view
]