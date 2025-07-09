from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello, World!')

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'gallery/index.html', {'products': products})