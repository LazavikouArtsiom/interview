from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from cart.models import Cart
from .serializers import CartItemsSerializer, CartItemsDetailSerializer, CartItemCreateSerializer
from cart.selectors import get_cart_items_by_user
from cart.services import create_new_cart_item_for_user


@permission_classes([IsAuthenticated])
class CartItemsListCreateApi(ListCreateAPIView):

    def get_queryset(self):
        user = self.request.user
        return get_cart_items_by_user(user)

    def post(self, request, *args, **kwargs):
        status = create_new_cart_item_for_user(self, request, *args, **kwargs)
        return Response(status=status)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if hasattr(self.request, 'method'):
            if self.request.method == 'GET':
                return CartItemsSerializer
            if self.request.method == 'POST':
                return CartItemCreateSerializer


@permission_classes([IsAuthenticated])
class CartItemsRetrieveUpdateDestoyApi(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemsDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return get_cart_items_by_user(user)
