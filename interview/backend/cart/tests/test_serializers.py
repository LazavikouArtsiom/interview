from collections import OrderedDict

from django.test import TestCase

from cart.api.v1.serializers import (CartItemCreateSerializer, CartItemDetailSerializer,
                                     CartItemsSerializer, )
from users.models import User
from products.models import (Sale, Category, Product)
from cart.models import Cart, CartItem

class CartSerializersTest(TestCase):
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
                                quantity=1,
                                )
        self.cart_item = CartItem.objects.get(cart=self.cart)

    def test_cart_item_create_serializer(self):
        data = CartItemCreateSerializer(instance=self.cart_item).data
        expected_data = {'product': OrderedDict([('slug', 'name')]),
                         'quantity': 1, 
                         'url': self.cart_item.get_absolute_url()}
        self.assertEqual(expected_data, data)

    def test_cart_item_detail_serializer(self):
        data = CartItemDetailSerializer(instance=self.cart_item).data
        expected_data = {'product': OrderedDict([
                            ('slug', 'name'),
                            ('name', 'name'),
                            ('price', '1000.00'),
                            ('category', 'name'),
                            ('total_price', 1000.0),
                            ('sales', {}),
                            ('id', self.cart_item.id),
                            ('url', self.product.get_absolute_url())
                        ]),
                        'quantity': 1}
        self.assertEqual(expected_data, data)

    def test_cart_items_serializer(self):
        data = CartItemsSerializer(instance=self.cart_item).data
        expected_data = {'product': OrderedDict([
                            ('slug', 'name'),
                            ('name', 'name'),
                            ('price', '1000.00'),
                            ('category', 'name'),
                            ('total_price', 1000.0),
                            ('sales', {}),
                            ('id', self.cart_item.id),
                            ('url', self.product.get_absolute_url())
                        ]),
                        'quantity': 1,
                        'url': self.cart_item.get_absolute_url()
                        }
        self.assertEqual(expected_data, data)
