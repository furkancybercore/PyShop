# PyShop - Django E-commerce Project Reference Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Project Setup](#project-setup)
   - [Environment Setup](#environment-setup)
   - [Django Project Creation](#django-project-creation)
   - [Git Repository Setup](#git-repository-setup)
3. [Django App Development](#django-app-development)
   - [Creating the Products App](#creating-the-products-app)
   - [URL Mapping and Views](#url-mapping-and-views)
   - [Models and Database Design](#models-and-database-design)
   - [Database Migrations](#database-migrations)
4. [Admin Interface Customization](#admin-interface-customization)
   - [Admin Panel Setup](#admin-panel-setup)
   - [Customizing Model Display](#customizing-model-display)
5. [Frontend Development](#frontend-development)
   - [Templates and Template Tags](#templates-and-template-tags)
   - [Bootstrap Integration](#bootstrap-integration)
6. [Collaborative Workflow](#collaborative-workflow)
   - [Git Workflow Best Practices](#git-workflow-best-practices)
   - [Handling Merge Conflicts](#handling-merge-conflicts)
7. [Additional Resources](#additional-resources)

## Introduction

PyShop is a Django-based e-commerce project that demonstrates fundamental Django concepts such as:
- URL mapping
- Views and templates
- Models and database operations
- Admin interface customization

This README serves as a comprehensive notebook for Django development practices, documenting each step in the development process with explanations of key concepts.

## Project Setup

### Environment Setup

Start by setting up a clean development environment:

```bash
# Clone the repository
git clone https://github.com/furkancybercore/PyShop

# Navigate to project directory
cd PyShop/

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Django
pip install django
```

> **Note:** Always use virtual environments for Python projects to keep dependencies isolated.

### Django Project Creation

Create a new Django project:

```bash
# Create new Django project called 'pyshop'
django-admin startproject pyshop

# Test the development server
python3 manage.py runserver
```

The server will start at http://127.0.0.1:8000/. Press Ctrl+C to stop it.

### Git Repository Setup

Set up Git branching to manage development:

```bash
# Check current branches
git branch

# Create and switch to 'dev' branch
git checkout -b dev

# Add changes to staging
git add .

# Commit changes
git commit -m "Created pyshop project in Django"

# Push to remote repo and set upstream
git push -u origin dev
```

> **Best Practice:** Use a `dev` branch for development and merge to `main` only when features are complete and tested.

## Django App Development

### Creating the Products App

Django projects consist of multiple apps. Let's create a products app:

```bash
python3 manage.py startapp products

# Start server to test
python3 manage.py runserver
```

After creating the app, add it to Git:

```bash
git add .
git commit -m "created products app"
git push
```

### URL Mapping and Views

#### Creating First View

In `products/views.py`, create the index view:

```python
from django.shortcuts import render
from django.http import HttpResponse

"""
All views functions always take a request object parameter.
When a URL is accessed, HTTP sends a request, and Django passes
this request object to the view function.
"""
def index(request):
    return HttpResponse('Hello World')
```

#### Setting Up URL Patterns

Create a new file `products/urls.py` to define URL patterns for the products app:

```python
from django.urls import path
from . import views  # Import views from the same directory

"""
We create a list object to define our URL patterns
"""
urlpatterns = [
    path('', views.index),  # Root path maps to the index view
]
```

#### Connecting to Main URLs

In the main `pyshop/urls.py`, include the products app URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))  # When user visits /products/, Django will use patterns from products.urls
]
```

#### Adding More Routes

Add a new route for displaying new products:

1. Add to `products/urls.py`:
```python
urlpatterns = [
    path('', views.index),
    path('new', views.new)  # Maps /products/new/ to the new view
]
```

2. Add the corresponding view in `products/views.py`:
```python
def new(request):
    return HttpResponse('New Products')
```

Commit your changes:
```bash
git add .
git commit -m "added /product/new directory"
git push
```

### Models and Database Design

Models define your database structure. In `products/models.py`:

```python
from django.db import models

class Product(models.Model):
    """
    Product model represents items for sale in our shop
    """
    name = models.CharField(max_length=255)  # Product name with max length
    price = models.FloatField()  # Price as a decimal number
    stock = models.IntegerField()  # Quantity in stock
    image_url = models.CharField(max_length=2083)  # URL to product image
                                                  # 2083 is max URL length
```

Commit your model changes:
```bash
git add README.md products/models.py
git commit -m "updated products/models.py"
git push
```

### Database Migrations

Django uses migrations to update the database schema when models change:

1. First, register your app in `pyshop/settings.py`:
```python
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Our apps
    'products.apps.ProductsConfig',  # Register the products app
]
```

2. Create migrations:
```bash
python3 manage.py makemigrations
```

This command creates migration files in `products/migrations/` that define how to update the database.

3. Apply migrations:
```bash
python3 manage.py migrate
```

This command executes the migrations and updates the database schema.

#### Adding Additional Models

Let's add an Offer model for discounts:

```python
class Offer(models.Model):
    """
    Offer model represents discount offers for products
    """
    code = models.CharField(max_length=10)  # Coupon code
    description = models.CharField(max_length=255)  # Offer description
    discount = models.FloatField()  # Discount amount
```

Create and apply migrations for the new model:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Commit your changes:
```bash
git add .
git commit -m "created offer class"
git push
```

## Admin Interface Customization

### Admin Panel Setup

Django provides a built-in admin interface:

1. Start the server:
```bash
python3 manage.py runserver
```

2. Create a superuser to access the admin panel:
```bash
python3 manage.py createsuperuser
# Enter username, email, and password when prompted
```

3. Access the admin interface at http://127.0.0.1:8000/admin/

### Customizing Model Display

To make models visible in the admin interface, update `products/admin.py`:

```python
from django.contrib import admin
from .models import Product, Offer

class ProductAdmin(admin.ModelAdmin):
    """
    Customizes how Products appear in the admin interface
    """
    list_display = ('name', 'price', 'stock')  # Fields to display in the list view

class OfferAdmin(admin.ModelAdmin):
    """
    Customizes how Offers appear in the admin interface
    """
    list_display = ('code', 'discount')  # Fields to display in the list view

# Register models with the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
```

#### Customizing Model Names

To customize how model names appear in the admin interface, add a Meta class to your models:

```python
class Product(models.Model):
    # Fields remain the same
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Offer(models.Model):
    # Fields remain the same
    
    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"
```

Commit your changes:
```bash
git add .
git commit -m "Customized Admin Panel"
git push origin dev
```

## Frontend Development

### Templates and Template Tags

Django uses templates to generate HTML. Create a templates directory:

```bash
mkdir -p products/templates/
```

Create `products/templates/index.html`:

```html
<h1>Products</h1>
<ul>
    {% for product in products %}
        <li>{{ product.name }} - {{ product.price }}</li>
    {% endfor %}
</ul>
```

Update your view to use the template:

```python
from .models import Product

def index(request):
    products = Product.objects.all()  # Fetch all products from database
    return render(request, 'index.html', {'products': products})
    """
    render function:
    1. First argument: request object
    2. Second argument: template name (Django looks in app's templates directory)
    3. Third argument: context dictionary (data to pass to the template)
    """
```

### Bootstrap Integration

To add Bootstrap and improve the UI, update your template:

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

## Collaborative Workflow

### Git Workflow Best Practices

When working on a team project, follow these best practices:

1. Always pull the latest changes before starting work:
```bash
git checkout dev
git pull origin dev
```

2. Create feature branches for new work:
```bash
git checkout -b feature/my-new-feature
```

3. Make frequent, small commits with descriptive messages:
```bash
git add .
git commit -m "Implemented product filtering by category"
```

4. Push changes to remote:
```bash
git push -u origin feature/my-new-feature
```

5. Create a pull request on GitHub to merge changes to the dev branch

### Handling Merge Conflicts

If others have made changes to the same files you've modified, you might encounter merge conflicts:

1. Pull the latest changes and merge them with yours:
```bash
git checkout dev
git pull origin dev
git checkout feature/my-new-feature
git merge dev
```

2. If there are conflicts, Git will indicate which files have conflicts. Open those files to resolve the conflicts:
```
<<<<<<< HEAD
Your changes
=======
Remote changes
>>>>>>> branch-name
```

3. Edit the files to keep the desired code and remove the conflict markers

4. After resolving all conflicts, commit the merged changes:
```bash
git add .
git commit -m "Resolved merge conflicts"
git push
```

## Additional Resources

For more detailed information about the code used in this project, see [CODE_REFERENCE.md](CODE_REFERENCE.md).

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Model Field Reference](https://docs.djangoproject.com/en/stable/ref/models/fields/)
- [Django Admin Customization](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
- [Git Workflow Guide](https://www.atlassian.com/git/tutorials/comparing-workflows)