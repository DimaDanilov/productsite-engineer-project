from .models import Products
from django.forms import ModelForm, TextInput, Select, Textarea, NumberInput


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["title", "brand", "productGroup", "description", "price"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название продукта...'
            }),
            "brand": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фирмы...'
            }),
            "productGroup": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите отдел продукта...'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание продукта...'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену...'
            })
        }