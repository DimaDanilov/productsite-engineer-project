from django.shortcuts import render
from .models import Products
from .forms import ProductForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error="Форма не валидна"

    products = Products.objects.all()
    form = ProductForm()
    context = {
        'products': products,
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', context)