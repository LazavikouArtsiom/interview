from rest_framework import serializers

from orders.models import Order
from cart.api.v1.serializers import CartSerializer


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['delivery', 'delivery_address', 'phone_number']


class OrderListSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['delivery',
                  'delivery_address',
                  'phone_number',
                  'cart',
                  'status',
                  'total_cost',
                  ]

