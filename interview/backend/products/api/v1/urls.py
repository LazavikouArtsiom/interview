from django.urls import path, include
from .views import (CategoryListApi, ProductsListByCategoryApi,
                    ProductRetrieveApi,
                    )

urlpatterns = [
    path('', CategoryListApi.as_view(), name='category-list'),
    path('<slug:category_slug>/', ProductsListByCategoryApi.as_view(),
         name='products-list-by-category'),
    path('<slug:category_slug>/<slug:slug>/',
         ProductRetrieveApi.as_view(), name='product-detail'),
]
