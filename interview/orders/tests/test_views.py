from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import login

from products.models import Category, Product
from cart.models import Cart, CartItem
from users.models import User


class OrdersViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                   )
        self.client.force_login(User.objects.get(username='username',
                                                 password='password',
                                                 ))
        self.category = Category.objects.create(name='name',
                                                slug='slug',
                                                )
        self.product = Product.objects.create(name='name',
                                              slug='name',
                                              price=1000,
                                              category=self.category,
                                              )
        self.cart = Cart.objects.get(user=self.user, status='new')
        self.cart_item = CartItem.objects.create(product=self.product,
                                                 cart=self.cart,
                                                 quantity=1)

    def test_order_creation(self):
        response = self.client.get(reverse('order-list',))
        self.assertEqual(response.status_code, 200)
