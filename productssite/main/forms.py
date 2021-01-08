from .models import Products
from django.forms import ModelForm, TextInput, Select, Textarea, NumberInput


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["title", "brand", "productGroup", "description", "price"]
        widgets = {
            "title": TextInput(attrs={
                'id': 'title',
                'class': 'form-control',
                'placeholder': 'Введите название продукта...'
            }),
            "brand": TextInput(attrs={
                'id': 'brand',
                'class': 'form-control',
                'placeholder': 'Введите название фирмы...'
            }),
            "productGroup": Select(attrs={
                'id': 'productGroup',
                'class': 'form-control',
                'placeholder': 'Выберите отдел продукта...'
            }),
            "description": Textarea(attrs={
                'id': 'description',
                'class': 'form-control',
                'placeholder': 'Введите описание продукта...'
            }),
            "price": NumberInput(attrs={
                'id': 'price',
                'class': 'form-control',
                'placeholder': 'Введите цену...'
            })
        }