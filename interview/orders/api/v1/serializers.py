from rest_framework import serializers

from orders.models import Order

class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['delivery', 'delivery_address', 'phone_number']


class OrdersListSerializer(serializers.ModelSerializer):
    cart = serializers.CharField(source='cart.id')

    class Meta:
        model = Order
        fields = ['id',
                  'delivery',
                  'delivery_address',
                  'phone_number',
                  'cart',
                  'status',
                  'total_cost',
                  ]
