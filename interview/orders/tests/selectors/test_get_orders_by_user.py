from django.test import TestCase
from django.contrib.auth.models import User

from cart.models import Cart, CartItem
from products.models import Product, Category
from orders.models import Order
from orders.selectors import get_orders_by_user


class GetOrdersByUserTest(TestCase):
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
                                quantity=1,
                                )
        self.cart_items = CartItem.objects.filter(cart=self.cart)
        Order.objects.create(user=self.user, cart=self.cart)
        self.orders = Order.objects.filter(user=self.user)


    def test_get_orders_by_user(self):
        self.assertEqual(list(get_orders_by_user(self.user)),
                         list(self.orders))
