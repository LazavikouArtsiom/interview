from django.test import TestCase
from users.models import User

from cart.models import Cart, CartItem
from products.models import Product, Category
from cart.selectors import _get_all_cart_items_for_cart


class SignalTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )

    def test_user_creation_calls_cart_creating_signal(self):
        self.assertIsNotNone(Cart.objects.get(user=self.user))
