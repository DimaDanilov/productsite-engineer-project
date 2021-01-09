from django.shortcuts import render
from .models import Products
from .serializers import ProductsSerializer
from .forms import ProductForm
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductsView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response({"products": serializer.data})


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