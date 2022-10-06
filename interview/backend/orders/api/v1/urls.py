from django.urls import path
from .views import OrderListCreateApi

urlpatterns = [
    path('', OrderListCreateApi.as_view(), name='order-list'),
]
