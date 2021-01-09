from django.urls import path
from . import views
from .views import ProductsView


app_name = "products"

urlpatterns = [
    path('', views.index),
    path('products', views.ProductsView.as_view())
]