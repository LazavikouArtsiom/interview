from django.test import TestCase

from products.api.v1.serializers import (CategorySerializer,
                                         ProductsListSerializer, ProductCreateSerializer, ProductRetrieveSerializer,
                                         )
from products.models import (Sale, Category, Product)


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

    def test_category_serializer(self):
        data = CategorySerializer(instance=self.category).data
        expected_data = {
            'name': self.category.name,
            'url': self.category.get_absolute_url()
        }
        self.assertEqual(expected_data, data)

    def test_products_list_serializer(self):
        data = ProductsListSerializer(instance=self.product).data
        expected_data = {'slug': 'name',
                         'name': 'name',
                         'price': '1000.00',
                         'category': 'name',
                         'total_price': 1000.0,
                         'sales': {},
                         'id': self.product.id,
                         'url': self.product.get_absolute_url()
                         }
        self.assertEqual(expected_data, data)

    def test_product_create_serializer(self):
        data = ProductCreateSerializer(instance=self.product).data
        expected_data = {
            'slug': self.product.slug
        }
        self.assertEqual(expected_data, data)

    def test_product_retrieve_serializer(self):
        data = ProductRetrieveSerializer(instance=self.product).data
        expected_data ={
            'slug': 'name',
            'name': 'name',
            'price': '1000.00',
            'category': 'name',
            'total_price': 1000.0,
            'sales': '{}',
            'id': self.product.id,
        }
        self.assertEqual(expected_data, data)
