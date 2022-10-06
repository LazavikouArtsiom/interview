from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, transaction

from products.models import Product
from cart.models import CartItem
from .selectors import _get_cart_by_user, _get_all_cart_items_for_cart

from rest_framework.response import Response
from rest_framework import status


def create_new_cart_item_for_user(self, request, *args, **kwargs) -> status:
    try:
        cart = _get_cart_by_user(self.request.user)
        items = _get_all_cart_items_for_cart(cart=cart)
        slug = request.data['product.slug']
        quantity = request.data['quantity']
        product = Product.objects.get(slug=slug)
        with transaction.atomic():
            CartItem.objects.create(cart=cart, product=product, quantity=quantity)
        return status.HTTP_201_CREATED
    except (ObjectDoesNotExist, IntegrityError):
        return status.HTTP_400_BAD_REQUEST
