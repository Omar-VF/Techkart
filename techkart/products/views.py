from django.shortcuts import render
from .models import Product

# Create your views here.


def home(request):
    return render(request, "index.html")


def products(request):
    product_list = Product.objects.all()
    products = {"products": product_list}
    return render(request, "products.html", products)


def details(request):
    return render(request, "product_details.html")
