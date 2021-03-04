from django.test import TestCase
from django.contrib.auth.models import User

from cart.models import Cart, CartItem
from products.models import Product, Category
from orders.models import Order
from products.selectors import get_products_by_slug


class GetProductsBySlugTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='name',
                                                slug='slug',
                                                )
        self.product = Product.objects.create(name='name',
                                              slug='name',
                                              price=1000,
                                              category=self.category,
                                              )


    def test_get_products_by_slug(self):
        self.assertEqual(list(get_products_by_slug(self.product.slug)),
                         list(Product.objects.filter(slug=self.product.slug)))

