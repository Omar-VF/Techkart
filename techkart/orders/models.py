from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.


# model for order
class Order(models.Model):
    LIVE = 1
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICES = (
        (CART_STAGE, "CART_STAGE"),
        (ORDER_CONFIRMED, "ORDER_CONFIRMED"),
        (ORDER_PROCESSED, "ORDER_PROCESSED"),
        (ORDER_DELIVERED, "ORDER_DELIVERED"),
        (ORDER_REJECTED, "OREDER_REJECTED"),
    )
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    total_price = models.FloatField(default=0)
    owner = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, related_name="orders"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Order ID : {self.id}"


# model for ordered item
class OrderedItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="added_carts"
    )
    quantity = models.IntegerField(null=True)
    owner = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="added_items"
    )

    def __str__(self) -> str:
        return self.product.title

    def orderid(self):
        orderid = self.owner.id
        return orderid
