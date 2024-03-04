from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    featured_products = Product.objects.order_by('-priority')[:4]
    latest_products = Product.objects.order_by('-created_at')[:8]
    context = {
        'featured_products':featured_products,
        'latest_products':latest_products
    }

    return render(request, "index.html",context)


# Products page
def products(request):
    # Switching between pages
    page = 1
    if request.GET:
        page = request.GET.get("page", 1)
    else:
        pass

    product_list = Product.objects.order_by('-priority')
    item_paginator = Paginator(product_list, 4)
    product_list = item_paginator.get_page(page)
    products = {"products": product_list}

    return render(request, "products.html", products)


def details(request,pk):
    product = Product.objects.get(pk=pk)
    context = {'product':product}

    return render(request, "product_details.html",context)
