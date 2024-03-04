from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    return render(request, "index.html")


# Products page
def products(request):
    # Switching between pages
    page = 1
    if request.GET:
        page = request.GET.get("page", 1)
    else:
        pass

    product_list = Product.objects.all()
    item_paginator = Paginator(product_list, 3)
    product_list = item_paginator.get_page(page)
    products = {"products": product_list}

    return render(request, "products.html", products)


def details(request,pk):
    product = Product.objects.get(pk=pk)
    context = {'product':product}

    return render(request, "product_details.html",context)
