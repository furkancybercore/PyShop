# PyShop Code Reference

This document provides a concise explanation of the code used in the PyShop project. For more detailed explanations and step-by-step instructions, refer to the [README.md](README.md).

## Table of Contents

1. [Project Structure](#project-structure)
2. [Models](#models)
3. [Views](#views)
4. [URL Patterns](#url-patterns)
5. [Admin Interface](#admin-interface)
6. [Templates](#templates)

## Project Structure

PyShop follows the standard Django project structure:

```
PyShop/
├── manage.py              # Django's command-line utility for administrative tasks
├── pyshop/                # Main project directory
│   ├── __init__.py        # Marks directory as Python package
│   ├── settings.py        # Project settings
│   ├── urls.py            # Project URL configuration
│   ├── asgi.py            # ASGI configuration for deployment
│   └── wsgi.py            # WSGI configuration for deployment
└── products/              # Products app directory
    ├── __init__.py        # Marks directory as Python package
    ├── admin.py           # Admin interface configuration
    ├── apps.py            # App configuration
    ├── migrations/        # Database migrations
    ├── models.py          # Data models
    ├── tests.py           # Test cases
    ├── urls.py            # App URL configuration
    ├── views.py           # View functions/classes
    └── templates/         # HTML templates
        └── index.html     # Product listing template
```

## Models

### Product Model

```python
class Product(models.Model):
    name = models.CharField(max_length=255)      # Product name
    price = models.FloatField()                  # Product price
    stock = models.IntegerField()                # Available quantity
    image_url = models.CharField(max_length=2083) # URL to product image
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
```

### Offer Model

```python
class Offer(models.Model):
    code = models.CharField(max_length=10)       # Discount code (e.g., "SUMMER10")
    description = models.CharField(max_length=255) # Offer description
    discount = models.FloatField()               # Discount amount
    
    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"
```

## Views

### Product List View

```python
def index(request):
    # Fetch all products from the database
    products = Product.objects.all()
    
    # Render the index template with the products
    return render(request, 'index.html', {'products': products})
```

### New Products View

```python
def new(request):
    # Simple response for the new products page
    return HttpResponse('New Products')
```

## URL Patterns

### App-level URLs (products/urls.py)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),     # Root path (/products/) maps to index view
    path('new', views.new)     # /products/new/ maps to new view
]
```

### Project-level URLs (pyshop/urls.py)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),             # Admin interface
    path('products/', include('products.urls'))  # Include the products app URLs
]
```

## Admin Interface

### Product Admin Configuration

```python
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')  # Fields to display in the list view

admin.site.register(Product, ProductAdmin)
```

### Offer Admin Configuration

```python
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')  # Fields to display in the list view

admin.site.register(Offer, OfferAdmin)
```

## Templates

### Product Listing Template (index.html)

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

## Django Commands Reference

| Command | Description |
|---------|-------------|
| `python3 -m venv venv` | Create a virtual environment |
| `source venv/bin/activate` | Activate the virtual environment |
| `pip install django` | Install Django |
| `django-admin startproject projectname` | Create a new Django project |
| `python manage.py startapp appname` | Create a new Django app |
| `python manage.py runserver` | Start the development server |
| `python manage.py makemigrations` | Create database migrations |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py createsuperuser` | Create an admin user |
| `python manage.py shell` | Open Django shell |

## Git Commands Reference

| Command | Description |
|---------|-------------|
| `git clone <url>` | Clone a repository |
| `git checkout -b <branch>` | Create and switch to a new branch |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit staged changes |
| `git push -u origin <branch>` | Push to remote and set upstream |
| `git pull origin <branch>` | Pull changes from remote |
| `git merge <branch>` | Merge a branch into current branch | 