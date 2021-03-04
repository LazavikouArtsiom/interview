from django.db.models.query import QuerySet
from django.contrib.auth.models import User

from cart.selectors import _get_cart_by_user, _get_all_cart_items_for_cart
from orders.models import Order
from cart.models import Cart


def _get_total_cost_for_cart(cart_id: int) -> int:
    """
        Iterates through CartItems in cart and calculates
        price 
    """
    cart_items = _get_all_cart_items_for_cart(cart_id)
    price = sum([cart_item.product.price *
                 cart_item.quantity for cart_item in cart_items])
    return price


def _create_new_cart_for_user(user: User) -> None:
    """
        Creates new cart when old ones status
        is set to old
    """
    return Cart.objects.create(user=user)


def _change_cart_status(cart: Cart) -> None:
    """
        Changes cart status to old to avoid
        more then one use of this cart in order
    """
    cart.status = 'old'
    cart.save()


def create_order(self, user: User) -> QuerySet[Order]:
    """
        Creates new Order
        changes cart_status using _change_cart_status()
        creates new cart for user using _create_new_cart_for_user()
    """
    cart = _get_cart_by_user(user)

    if self.request.data['delivery'] == 'true':
        delivery = True
    else:
        delivery = False

    delivery_address = self.request.data['delivery_address']
    phone_number = self.request.data['phone_number']
    total_cost = _get_total_cost_for_cart(cart)
    order = Order.objects.create(user=user,
                                 cart=cart,
                                 delivery=delivery,
                                 delivery_address=delivery_address,
                                 phone_number=phone_number,
                                 total_cost=total_cost)
    _change_cart_status(cart)
    _create_new_cart_for_user(user)
    return order
