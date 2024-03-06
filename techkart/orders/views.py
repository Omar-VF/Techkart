from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderedItem
from products.models import Product
from django.contrib import messages

# Create your views here.


@login_required(login_url="register")
def cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
        owner=customer, order_status=Order.CART_STAGE
    )
    context = {"cart": cart_obj}

    return render(request, "cart.html", context)


def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile

        quantity = request.POST.get("quantity")
        product_id = request.POST.get("product_id")

        cart_obj, created = Order.objects.get_or_create(
            owner=customer, order_status=Order.CART_STAGE
        )

        product = Product.objects.get(pk=product_id)
        ordered_item, created = OrderedItem.objects.get_or_create(
            product_id=product.id, owner=cart_obj
        )
        if created:
            ordered_item.quantity = int(quantity)
            ordered_item.save()
        else:
            ordered_item.quantity = ordered_item.quantity + int(quantity)
            ordered_item.save()

        return redirect("cart")


# function to remove a product from the cart
def remove_cart_item(request, pk):
    item = OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()

    return redirect("cart")


# Checkout func -> func to place the cart order
def checkout(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile

            total = float(request.POST.get("total"))

            order_obj = Order.objects.get(owner=customer, order_status=Order.CART_STAGE)

            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()

                status_message = "Your order has been confirmed! It will be delivered to you shortly!"
                messages.success(request, status_message)

            else:
                status_message = "Unable to proceed! No Items in cart!"
                messages.error(request, status_message)
        except Exception as e:
            status_message = "Error : Unable to proceed!"
            messages.error(request, status_message)

    return redirect("cart")
