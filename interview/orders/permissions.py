from rest_framework import permissions
from .services import _get_cart_by_user, _get_all_cart_items_for_cart

class hasItemsInCart(permissions.BasePermission):
    """
       User must have items in cart to create order
    """
    message = 'Customer must have any items in cart'

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            cart = _get_cart_by_user(request.user)
            if not _get_all_cart_items_for_cart(cart):
                return False
            else:
                return True

        