from django.contrib import admin

# Register your models here.
from products.models import Category, Products

admin.site.register(Category)
admin.site.register(Products)