from cart.models import Cart
from django.core.exceptions import ObjectDoesNotExist

from orders.services import _create_new_cart_for_user, _change_cart_status_to_old

def calculate_total_cost_for_order(sender, instance, created, **kwargs):
    _create_new_cart_for_user(user=instance.user)
