from django.test import TestCase
from django.urls import reverse
from products.models import Category, Product

class ProductsListByCategoryApiTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='name',
                                                slug='slug',
                                                )

    def test_products_list_by_category_api(self):
        response = self.client.get(reverse('products-list-by-category',
                                            kwargs={'category_slug':self.category.slug}))
        self.assertEqual(response.status_code, 200)