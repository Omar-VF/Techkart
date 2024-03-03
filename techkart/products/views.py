from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")

def products(request):
    return render(request,'products.html')

def details(request):
    return render(request,'product_details.html')