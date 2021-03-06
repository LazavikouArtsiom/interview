from django.db import models
from django.conf import settings

from cart.models import Cart


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
