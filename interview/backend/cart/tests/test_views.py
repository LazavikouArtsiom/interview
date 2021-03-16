import json

from django.test import TestCase
from django.urls import reverse

from users.models import User
from products.models import Product, Category, Sale
from cart.services import create_new_cart_item_for_user
from cart.models import CartItem, Cart


class CartViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )
        self.client.force_login(User.objects.get(username='username',
                                                 password='password',
                                                 ))
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
        self.cart = Cart.objects.get(user=self.user, status='new')

    def test_cart_items_list_api(self):
        response = self.client.get(reverse('cart-items-list'))
        self.assertEqual(response.status_code, 200)

    def test_cart_items_create_with_existing_product_api(self):
        self.data = {
            'product.slug': self.product.slug,
            "quantity": 1,
        }
        response = self.client.post(reverse('cart-items-list'), data=self.data)
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(response.status_code, 201)

    def test_cart_items_create_with_not_existing_product_api(self):
        self.data = {
            'product.slug': "some-not-existing-slug",
            "quantity": 1,
        }
        response = self.client.post(reverse('cart-items-list'), data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_cart_items_create_with_already_existing_product_api(self):
        CartItem.objects.create(product=self.product,
                                cart=self.cart,
                                quantity=1)
        self.data = {
            'product.slug': self.product.slug,
            "quantity": 1,
        }
        response = self.client.post(reverse('cart-items-list'), data=self.data)
        self.assertEqual(response.status_code, 400)

    def test_cart_items_retrieve_api(self):
        cart_item = CartItem.objects.create(product=self.product,
                                            cart=self.cart,
                                            quantity=1)
        response = self.client.get(
            reverse('cart-items-retrieve-update-delete', kwargs={'id': cart_item.id}))
        self.assertEqual(response.status_code, 200)

    def test_cart_items_destroy_api(self):
        cart_item = CartItem.objects.create(product=self.product,
                                            cart=self.cart,
                                            quantity=1)
        response = self.client.delete(
            reverse('cart-items-retrieve-update-delete', kwargs={'id': cart_item.id}))
        self.assertEqual(response.status_code, 204)

    def test_cart_items_update_api(self):
        cart_item = CartItem.objects.create(product=self.product,
                                            cart=self.cart,
                                            quantity=1)
        data = json.dumps({'quantity': '11'})
        response = self.client.put(reverse('cart-items-retrieve-update-delete',
                                           kwargs={'id': cart_item.id}), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 302)
        cart_item.refresh_from_db()
        self.assertEqual(cart_item.quantity, 11)
