from django.db.models.query import QuerySet
from django.contrib.auth.models import User

from orders.models import Order


def get_orders_by_user(user: User) -> QuerySet[Order]:
    """
        Filtering Orders by throwed user instance
    """
    return Order.objects.select_related('user', 'cart').filter(user=user)
