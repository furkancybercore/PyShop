# PyShop Code Reference

This document provides a concise explanation of the code used in the PyShop e-commerce project.

## Project Structure

```
PyShop/
├── manage.py              # Django's command-line utility for administrative tasks
├── pyshop/                # Main project directory
│   ├── __init__.py        # Makes pyshop a Python package
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL router
│   ├── asgi.py            # ASGI configuration
│   └── wsgi.py            # WSGI configuration
├── products/              # Products app directory
│   ├── __init__.py        # Makes products a Python package
│   ├── admin.py           # Admin interface configuration
│   ├── apps.py            # App configuration
│   ├── migrations/        # Database migrations
│   ├── models.py          # Database models
│   ├── templates/         # HTML templates
│   │   └── index.html     # Product listing template
│   ├── tests.py           # Test cases
│   ├── urls.py            # URL patterns for the app
│   └── views.py           # View functions
└── db.sqlite3             # SQLite database file
```

## Key Code Components

### Models (products/models.py)

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name
    price = models.FloatField()              # Product price
    stock = models.IntegerField()            # Available quantity
    image_url = models.CharField(max_length=2083)  # Product image URL
    
class Offer(models.Model):
    code = models.CharField(max_length=10)        # Offer code (e.g., "SUMMER10")
    description = models.CharField(max_length=255)  # Offer description
    discount = models.FloatField()                 # Discount amount (e.g., 0.2 for 20%)
```

These models define the database schema for the application. Django automatically creates database tables based on these model definitions.

### Views (products/views.py)

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()  # Get all products from database
    return render(request, 'index.html', {'products': products})  # Render template with products

def new(request):
    return HttpResponse('New Products')  # Simple text response
```

Views are responsible for processing requests and returning responses. The `index` view fetches all products and renders the `index.html` template. The `new` view returns a simple text response.

### URL Configuration (products/urls.py)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),     # Route root URL to index view
    path('new', views.new)     # Route /new URL to new view
]
```

This maps URL patterns to view functions within the products app.

### Main URL Configuration (pyshop/urls.py)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # Django admin URLs
    path('products/', include('products.urls'))  # Include products app URLs under /products/
]
```

This includes the products app URLs and sets up the Django admin URLs.

### Admin Configuration (products/admin.py)

```python
from django.contrib import admin
from .models import Product, Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')  # Fields to display in admin list view

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')  # Fields to display in admin list view

admin.site.register(Product, ProductAdmin)  # Register Product model with admin
admin.site.register(Offer, OfferAdmin)      # Register Offer model with admin
```

This code configures how models appear in the Django admin interface.

### Template (products/templates/index.html)

```html
<h1>Products</h1>
<ul>
    {% for product in products %}
        <li>{{ product.name }} - ${{ product.price }}</li>
    {% endfor %}
</ul>
```

This template uses Django's template language to iterate over the products and display their names and prices.

### Enhanced Template (with Bootstrap)

```html
<!DOCTYPE html>
<html>
<head>
    <title>PyShop</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1 class="mt-4">Products</h1>
                <div class="row">
                    {% for product in products %}
                        <div class="col-md-4 mb-4">
                            <div class="card">
                                <img src="{{ product.image_url }}" class="card-img-top" alt="{{ product.name }}">
                                <div class="card-body">
                                    <h5 class="card-title">{{ product.name }}</h5>
                                    <p class="card-text">${{ product.price }}</p>
                                    <p class="card-text">Stock: {{ product.stock }}</p>
                                    <a href="#" class="btn btn-primary">Add to Cart</a>
                                </div>
                            </div>
                        </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

This enhanced template uses Bootstrap to create a responsive grid layout with cards for each product.

## Key Django Concepts Used

1. **Models**: Define database structure using Python classes
2. **Views**: Handle HTTP requests and generate responses
3. **Templates**: Define the presentation layer using Django's template language
4. **URL Patterns**: Define URL routes and connect them to views
5. **Admin Interface**: Provides a built-in CRUD interface for models
6. **Migrations**: Track and apply database schema changes

## Common Django Commands

```bash
# Create a new project
django-admin startproject project_name

# Create a new app
python manage.py startapp app_name

# Create database migrations
python manage.py makemigrations

# Apply migrations to the database
python manage.py migrate

# Create a superuser for the admin interface
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Run Django shell (interactive Python shell with Django context)
python manage.py shell
``` 