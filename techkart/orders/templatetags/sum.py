from django import template

register = template.Library()


# Template tag for finding the total cost of all products in a cart
@register.simple_tag(name="sum")
def sum(cart):
    total = 0
    for item in cart.added_items.all():
        total += item.quantity * item.product.price

    return total