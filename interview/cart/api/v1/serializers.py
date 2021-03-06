from rest_framework import serializers

from cart.models import CartItem, Cart
from products.api.v1.serializers import ProductsListSerializer, ProductCreateSerializer


class CartSerializer(serializers.ModelSerializer):
    products = ProductsListSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        exclude = ['id', 'user', 'status']


class CartItemCreateSerializer(serializers.ModelSerializer):
    product = ProductCreateSerializer()
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'quantity',
                  'url',
                  ]


class CartItemsSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer()
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'quantity',
                  'url',
                  ]


class CartItemsDetailSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
