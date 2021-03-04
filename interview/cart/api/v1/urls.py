from django.urls import path

from .views import CartItemsListCreateApi, CartItemsRetrieveUpdateDestoyApi

urlpatterns = [
    path('', CartItemsListCreateApi.as_view(), name='cart-items-list'),
    path('<int:id>/', CartItemsRetrieveUpdateDestoyApi.as_view(), name='cart-items-retrieve-update-delete'),
]
