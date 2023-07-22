from django.contrib import admin

from .models import Category, Prices, Product, Catalog

admin.site.register(Catalog)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Prices)
