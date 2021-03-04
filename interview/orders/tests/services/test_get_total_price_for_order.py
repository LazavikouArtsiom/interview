from django.test import TestCase
from django.contrib.auth.models import User

from cart.models import Cart, CartItem
from products.models import Product, Category
from orders.models import Order
from orders.services import _get_total_cost_for_cart


class GetTotalCostForCartTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )
        self.category = Category.objects.create(name='name',
                                                slug='slug',
                                                )
        self.product = Product.objects.create(name='name',
                                              slug='name',
                                              price=1000,
                                              category=self.category,
                                              )
        self.cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=self.cart,
                                product=self.product,
                                quantity=2,
                                )

    def test_get_total_price(self):
        self.assertEqual(_get_total_cost_for_cart(self.cart), 2000)
