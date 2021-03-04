from django.test import TestCase
from django.contrib.auth.models import User

from cart.models import Cart, CartItem
from products.models import Product, Category
from orders.models import Order
from orders.services import _create_new_cart_for_user


class CreateNewCartForUserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )

    def test_create_new_cart_for_user(self):
        self.assertIn(_create_new_cart_for_user(self.user),
                      Cart.objects.filter(user=self.user)
                      )
