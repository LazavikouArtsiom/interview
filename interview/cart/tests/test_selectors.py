from django.test import TestCase

from users.models import User
from cart.models import Cart, CartItem
from products.models import Product, Category
from cart.selectors import (_get_all_cart_items_for_cart, _get_cart_by_user,
                            get_cart_items_by_user)


class CartSelectorsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )
        self.user_2 = User.objects.create(username='username2',
                                          password='password2',
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
        self.cart_items = CartItem.objects.filter(cart=self.cart)
        self.empty_cart = Cart.objects.create(user=self.user_2)

    def test_get_all_cart_items_for_not_empty_cart(self):
        self.assertEqual(list(_get_all_cart_items_for_cart(self.cart)),
                         list(self.cart_items))

    def test_get_all_cart_items_for_empty_cart(self):
        self.assertEqual(
            list(_get_all_cart_items_for_cart(self.empty_cart)), [])

    def test_get_cart_by_user(self):
        self.assertEqual(_get_cart_by_user(self.user), self.cart)

    def test_get_cart_items_by_user(self):
        self.assertEqual(list(get_cart_items_by_user(self.user)),
                         list(self.cart_items))
