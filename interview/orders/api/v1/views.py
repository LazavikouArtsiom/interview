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
    permission_classes = (hasItemsInCart,)

    def post(self, request, *args, **kwargs):
        create_order(self, self.request.user)
        return super().list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return get_orders_by_user(user)

    def get_serializer_class(self):
        if hasattr(self.request, 'method'):
            if self.request.method == 'GET':
                return OrderListSerializer
            if self.request.method == 'POST':
                return OrderCreateSerializer
