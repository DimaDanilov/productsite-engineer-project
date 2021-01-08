from django.contrib import admin
from .models import Brand, ProductGroup, Products, Salerman, Sale, SaleCheck


admin.site.register(Brand)
admin.site.register(ProductGroup)
admin.site.register(Products)
admin.site.register(Salerman)
admin.site.register(Sale)
admin.site.register(SaleCheck)