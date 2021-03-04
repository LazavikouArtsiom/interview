from django.shortcuts import render
from django.http import HttpResponseForbidden

from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from cart.models import Cart
from .serializers import CartItemsSerializer, CartItemsDetailSerializer
from cart.selectors import get_cart_items_by_user


@permission_classes([IsAuthenticated])
class CartItemsListCreateApi(ListCreateAPIView):
    serializer_class = CartItemsSerializer

    def get_queryset(self):
        user = self.request.user
        return get_cart_items_by_user(user)


@permission_classes([IsAuthenticated])
class CartItemsRetrieveUpdateDestoyApi(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemsDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return get_cart_items_by_user(user)
