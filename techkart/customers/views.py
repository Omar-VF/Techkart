from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages

# Create your views here.


def account(request):
    # Register
    if request.POST and "register" in request.POST:
        try:

            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            print(request.POST)

            # Create User Account
            user = User.objects.create(
                username=username, password=password, email=email
            )

            # Create Customer Account
            customer = Customer.objects.create(
                user=user, username=username, phone=int(phone), address=address
            )
            return redirect("home")

        except:

            errormsg = "Username Exists Or Invalid credentials"
            messages.error(request, errormsg)
            print(errormsg)


    elif request.POST and "login" in request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(request.POST)

    else:
        pass


    return render(request, "account.html")

    # Login


