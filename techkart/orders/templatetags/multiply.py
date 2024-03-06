from django import template

register = template.Library()


# Template tag for splitting the products to different rows
@register.simple_tag(name="multiply")
def multiply(x,y):
    return x*y