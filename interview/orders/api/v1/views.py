from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

from orders.models import Order
from cart.selectors import _get_cart_by_user
from orders.services import create_order
from orders.selectors import get_orders_by_user
from .serializers import OrderCreateSerializer, OrderListSerializer
from orders.permissions import hasItemsInCart


class OrderListCreateApi(ListCreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = (hasItemsInCart,)

    def post(self, request, *args, **kwargs):
        create_order(self, self.request.user)
        queryset = self.get_queryset()
        serializer = OrderListSerializer(queryset, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OrderListSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def get_queryset(self):
        user = self.request.user
        return get_orders_by_user(user)
    
