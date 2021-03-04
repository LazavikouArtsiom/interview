from django.db import models
from django.conf import settings

from products.models import Product


class Cart(models.Model):
    NEW = "new"
    OLD = "old"

    STATUSES = (
        (NEW, "New cart"),
        (OLD, "Old cart"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    products = models.ManyToManyField(Product, through='CartItem')

    status = models.CharField(
        max_length=10, choices=STATUSES, default=NEW)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.cart.id} | {self.product.name} | {self.quantity}'
