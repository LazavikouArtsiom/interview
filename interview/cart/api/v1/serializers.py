from rest_framework import serializers

from cart.models import CartItem, Cart
from products.api.v1.serializers import ProductListSerializer


class CartSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = Cart
        exclude = ['id', 'user', 'status']


class CartItemsSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'id']


class CartItemsDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
