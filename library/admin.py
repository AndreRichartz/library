from django.contrib import admin

from .models import Category, Publisher, Author, Book

# Register your models here.

admin.site.register(Category)

admin.site.register(Publisher)

admin.site.register(Author)

admin.site.register(Book)
