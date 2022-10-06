from django.db import models
from django.conf import settings

from cart.models import Cart
from django.db.models.signals import post_save
from .signals import calculate_total_cost_for_order

class Order(models.Model):
    NEW = "new"
    IN_PROCESS = "in_process"
    RENOUNCEMENT = "renouncement"
    COMPLETE = "complete"

    STATUSES = (
        (NEW, "New order"),
        (IN_PROCESS, "Order is in process"),
        (RENOUNCEMENT, "Order is declined"),
        (COMPLETE, "Order is complete"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='user',
    )
    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
        null=True,
        related_name='cart',
    )

    status = models.CharField(
        max_length=30, choices=STATUSES, default=NEW)

    delivery = models.BooleanField(default=False, null=True)
    delivery_address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=40, null=True)

    total_cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.id} | order'

    def save(self, *args, **kwargs):
        from orders.services import _get_total_cost_for_cart
        self.total_cost = _get_total_cost_for_cart(cart_id=self.cart.id)
        self.cart.status = 'old'
        self.cart.save()
        super(Order, self).save(*args, **kwargs)

post_save.connect(calculate_total_cost_for_order, sender=Order)
