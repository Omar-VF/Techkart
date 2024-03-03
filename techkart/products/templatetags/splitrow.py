from django import template

register = template.Library()


# Template tag for splitting the products to different rows
@register.filter(name="splitrow")
def splitrow(list, row_size):
    row = []
    i = 0
    for data in list:
        row.append(data)
        i += 1
        if i == row_size:
            yield row
            row = []
    yield row
