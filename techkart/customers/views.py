from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def account(request):

    # Register
    if request.POST and "register" in request.POST:
        try:

            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            address = request.POST.get("address")
            phone = int(request.POST.get("phone"))
            # Create User Account
            user = User.objects.create_user(
                username=username, password=password, email=email
            )
            # Create Customer Account
            customer = Customer.objects.create(
                user=user, username=username, phone=int(phone), address=address
            )
            succesmsg = "Successfully Registered!"
            messages.success(request, succesmsg)

        except Exception as e:
            errormsg = "Username Exists Or Invalid data!"
            messages.error(request, errormsg)

    # Login
    elif request.POST and "login" in request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")

        else:
            errormsg = "Username or Password Incorrect!"
            messages.error(request, errormsg)

    else:
        pass

    return render(request, "account.html")


def signout(request):
    logout(request)
    return redirect('home')