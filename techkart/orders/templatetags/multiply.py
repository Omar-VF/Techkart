from django import template

register = template.Library()


# Template tag for multiplying the price of products with the quantity
@register.simple_tag(name="multiply")
def multiply(x, y):
    return x * y
