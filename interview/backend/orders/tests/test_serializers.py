from django.test import TestCase

from orders.api.v1.serializers import OrderCreateSerializer, OrdersListSerializer
from users.models import User
from products.models import Sale, Category, Product
from orders.models import Order
from cart.models import Cart, CartItem


class OrdersSerializersTest(TestCase):
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
        self.sale = Sale.objects.create(name='10 percent sale',
                                        description='10ps desc',
                                        percent=10,
                                        )
        self.product = Product.objects.create(name='name',
                                              slug='name',
                                              price=1000,
                                              category=self.category,
                                              )
        self.product.sales.add(self.sale)
        self.product.save()
        self.cart = Cart.objects.get(user_id=self.user.id, status='new')
        self.cart_item = CartItem.objects.create(product=self.product,
                                                 cart=self.cart,
                                                 quantity=1)
        self.order = Order.objects.create(cart=self.cart,
                                          user=self.user,
                                          delivery=True,
                                          delivery_address='some street',
                                          phone_number='333333333')

    def test_order_create_serializer(self):
        data = OrderCreateSerializer(instance=self.order).data
        expected_data = {
            'delivery': True,
            'delivery_address': 'some street',
            'phone_number': '333333333'
            }
        self.assertEqual(expected_data, data)

    def test_order_list_serializer(self):
        data = OrdersListSerializer(instance=self.order).data
        expected_data = {
                        'id': self.order.id,
                        'delivery': True,
                        'delivery_address': 'some street',
                        'phone_number': '333333333',
                        'cart': str(self.cart.id),
                        'status': 'new',
                        'total_cost': 900.0
                        }
        self.assertEqual(expected_data, data)
