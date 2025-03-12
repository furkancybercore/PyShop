# PyShop
Here is the commands that i used in order. 

git clone https://github.com/furkancybercore/PyShop

cd PyShop/

python3 -m venv venv

source venv/bin/activate

pip install django

django-admin startproject pyshop

python3 manage.py runserver

ctrl + c

git branch

git checkout -b dev

git checkout -b dev

git add .

git commit -m "Created pyshop project in Django"

git push -u origin dev

git checkout main

git fetch origin

git pull origin main

git merge dev

git push origin main

git checkout dev

products/views.py
```
from django.shortcuts import render
from django.http import HttpResponse


"""
All views fuction always take parameter request object.
Because when we go to a link, http sents a request, 
this function takes this request object as an parameter.
"""
def index(request):
    return HttpResponse('Hello World')
```

## URL Mapping
create a new file named "urls.py" in products app

products/urls.py
```
from django.urls import path
from . import views # we imported views from the same directory


'''
we created this list oblect to keep our urls
'''
urlpatterns = [
    path('', views.index), # this is the path to the index view
]
```

there is an urls.py in pyshop. Its like parent.
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')) #we added this path. when user go this directory, it refer products.urls.py file.
]

```


products/urls.py;

* added "new" directory (http:.../products/new/)
```
    path('new',views.new) # this is "new" directory of products app
```


product/views.py;
we should add 'new' fuction that we mention in urls.py file
```
...
def new(request):
    return HttpResponse('New Products')
```

git add .
git commit -m "added /product/new directory"
git push

create a pull request and accept it in github.

### models

products/models.py;
```
class Product(models.Model): # Product is a class that inherits from models.Model
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
```