from django.test import TestCase

from users.models import User
from products.models import Product, Category, Sale
from products.services import get_sales_percent, calculate_price_with_sales


class ProductsServicesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )
        self.category = Category.objects.create(name='name',
                                                slug='slug')
        self.sale = Sale.objects.create(name='name',
                                        description='name',
                                        percent=10)
        self.product = Product.objects.create(name='name',
                                              slug='name',
                                              price=1000,
                                              category=self.category,
                                              )
        self.product.sales.add(self.sale)
        self.product.save()

    def test_get_sales_percent(self):
        self.assertEqual(get_sales_percent(self.product), 10)

    def test_calculate_price_with_sales(self):
        self.assertEqual(calculate_price_with_sales(self.product), 900)

    def test_calculate_price_with_sales_after_removing_sale(self):
        self.product.sales.remove(self.sale)
        self.assertEqual(calculate_price_with_sales(self.product), 1000)

    def test_calculate_price_with_sales_after_adding_sales(self):
        self.product.sales.add(self.sale)
        self.sale1 = Sale.objects.create(name='name1',
                                         description='name1',
                                         percent=15)
        self.product.sales.add(self.sale1)
        self.assertEqual(calculate_price_with_sales(self.product), 750)

