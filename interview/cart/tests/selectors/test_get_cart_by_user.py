from django.test import TestCase
from django.contrib.auth.models import User

from cart.models import Cart
from cart.selectors import _get_cart_by_user


class GetCartByUserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )
        self.cart = Cart.objects.create(user=self.user)

    def test_get_cart_by_user(self):
        self.assertEqual(_get_cart_by_user(self.user), self.cart)
