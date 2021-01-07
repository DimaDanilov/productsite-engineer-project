from django.contrib import admin
from .models import ProductGroup, Products, Salerman, Sale, SaleCheck


admin.site.register(ProductGroup)
admin.site.register(Products)
admin.site.register(Salerman)
admin.site.register(Sale)
admin.site.register(SaleCheck)