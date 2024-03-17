from collections.abc import Callable, Sequence
from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Order, OrderedItem

# Register your models here.


class OrderItem(admin.StackedInline):

    model = OrderedItem

    extra = 5

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj) -> bool:
        return False


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "owner",
        "total_price",
        "order_status",
        "created_at",
    ]

    readonly_fields = [
        "total_price",
        "owner",
    ]

    list_editable = [
        "order_status",
    ]

    list_filter = [
        "owner",
        "order_status",
    ]

    search_fields = (
        "owner__username",
        "id",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    inlines = [OrderItem]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["__str__", "quantity", "owner", "orderid"]

    list_filter = [
        "owner",
        "owner__id",
    ]

    search_fields = ("owner__id", "owner__owner__username", "product__title")

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedItem, OrderItemAdmin)
