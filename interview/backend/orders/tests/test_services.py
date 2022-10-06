from django.test import TestCase

from users.models import User
from cart.models import Cart, CartItem
from products.models import Product, Category
from orders.models import Order
from orders.services import (_change_cart_status_to_old, _create_new_cart_for_user,
                             _get_total_cost_for_cart)


class OrdersServicesTest(TestCase):
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
        self.cart = Cart.objects.get(user=self.user)
        CartItem.objects.create(cart=self.cart,
                                product=self.product,
                                quantity=2,
                                )

    def test_get_total_cost_for_cart(self):
        self.assertEqual(_get_total_cost_for_cart(self.cart), 2000)

    def test_create_new_cart_for_user(self):
        self.assertIn(_create_new_cart_for_user(self.user),
                      Cart.objects.filter(user=self.user)
                      )

    def test_change_cart_status_to_old(self):
        _change_cart_status_to_old(self.cart)
        self.assertEqual(self.cart.status, 'old')
