from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("addcart/", views.add_to_cart, name="addcart"),
    path("removeitem/<pk>", views.remove_cart_item, name="remove_item"),
    path("checkout/", views.checkout, name="checkout"),
    path("orders/", views.track_order, name="trackorder"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
