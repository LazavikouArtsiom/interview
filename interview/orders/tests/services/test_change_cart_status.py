from django.test import TestCase
from django.contrib.auth.models import User

from cart.models import Cart, CartItem
from products.models import Product, Category
from orders.models import Order
from orders.services import _change_cart_status


class ChangeCartStatus(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )
        self.cart = Cart.objects.create(user=self.user)

    def test_change_cart_status(self):
        _change_cart_status(self.cart)
        self.assertEqual(self.cart.status, 'old')
