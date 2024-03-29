from django.test import TestCase
from django.urls import reverse
from products.models import Category, Product


class ProductsViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='name',
                                                slug='slug',
                                                )
        self.product = Product.objects.create(name='name',
                                              slug='name',
                                              price=1000,
                                              category=self.category,
                                              )

    def test_products_list_by_category_api(self):
        response = self.client.get(reverse('product-detail',
                                           kwargs={'category_slug': self.category.slug,
                                                   'slug': self.product.slug,
                                                   }))
        self.assertEqual(response.status_code, 200)

    def test_category_list_api(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, 200)

    def test_products_list_by_category_api(self):
        response = self.client.get(reverse('products-list-by-category',
                                           kwargs={'category_slug': self.category.slug}))
        self.assertEqual(response.status_code, 200)
