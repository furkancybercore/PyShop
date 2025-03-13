# PyShop Code Documentation

This document provides a detailed explanation of the code used in the PyShop Django project. It serves as a reference for understanding the various components and their interactions.

## Project Structure

The project follows the standard Django structure:

```
PyShop/
├── manage.py
├── pyshop/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── products/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── 0001_initial.py
    ├── models.py
    ├── templates/
    │   └── index.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Django Settings

The `settings.py` file contains the configuration for the Django project. One important modification we made was adding our products app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products.apps.ProductsConfig',  # Our products app
]
```

## Models

### Product Model

The `Product` model represents the products available in our online store:

```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
```

- `name`: A CharField with a maximum length of 255 characters to store the product name
- `price`: A FloatField to store the product price
- `stock`: An IntegerField to store the quantity available
- `image_url`: A CharField with a maximum length of 2083 characters to store the URL of the product image
- The `Meta` inner class is used to customize the display name in the admin panel

### Offer Model

The `Offer` model represents special offers or discounts:

```python
class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    
    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"
```

- `code`: A CharField with a maximum length of 10 characters to store the offer code
- `description`: A CharField with a maximum length of 255 characters to store the offer description
- `discount`: A FloatField to store the discount percentage
- The `Meta` inner class is used to customize the display name in the admin panel

## URL Configuration

### Project URLs

The main URL configuration in `pyshop/urls.py` includes the admin site URLs and our products app URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))  # When user visits /products/, Django will look for URL patterns in products/urls.py
]
```

### Products App URLs

The URL configuration specific to the products app is defined in `products/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Maps /products/ to the index view
    path('new', views.new)  # Maps /products/new/ to the new view
]
```

## Views

The views are defined in `products/views.py`:

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(
        request, 
        'index.html',
        {'products': products}  # Pass products to the template as context
    )

def new(request):
    return HttpResponse('New Products')  # Simple text response
```

- `index`: This view fetches all products from the database and renders them using the `index.html` template
- `new`: This view returns a simple HttpResponse with the text "New Products"

## Templates

### index.html

The `index.html` template displays a list of products:

```html
<h1>Products</h1>
<ul>
    {% for product in products %}
        <li>{{ product.name }} - {{ product.price }}</li>
    {% endfor %}
</ul>
```

- Django template tags `{% %}` are used for control flow (like the for loop)
- Django template variables `{{ }}` are used to output the values of variables (like product.name)

## Admin Configuration

The admin configuration is defined in `products/admin.py`:

```python
from django.contrib import admin
from .models import Product, Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')  # Fields to display in the admin list view

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')  # Fields to display in the admin list view

admin.site.register(Product, ProductAdmin)  # Register Product model with its admin configuration
admin.site.register(Offer, OfferAdmin)  # Register Offer model with its admin configuration
```

- `ProductAdmin`: This class defines how the Product model should be displayed in the admin interface
- `OfferAdmin`: This class defines how the Offer model should be displayed in the admin interface
- `admin.site.register()`: This function registers our models with the admin site, optionally using a custom admin class

## Migrations

Django migrations are Python files that describe changes to your database schema. They're created with the `makemigrations` command and applied with the `migrate` command:

```bash
python manage.py makemigrations  # Create migration files
python manage.py migrate         # Apply migrations to the database
```

The initial migration file for our products app (`products/migrations/0001_initial.py`) defines the creation of the Product model:

```python
# Generated by Django 5.1.7 on 2025-03-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
```

## Common Django Commands

```bash
# Create a new Django project
django-admin startproject project_name

# Create a new app
python manage.py startapp app_name

# Run the development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell
```

## Next Steps

Here are some potential improvements or next steps for this project:

1. Add Bootstrap styling to the templates
2. Implement detail views for individual products
3. Add a shopping cart functionality
4. Implement user authentication and registration
5. Add payment processing
6. Create a search functionality
7. Implement product categories
8. Add product reviews and ratings 