from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from products.models import Category, Product
from products.selectors import get_products_by_category_slug, get_products_by_slug
from .serializers import CategorySerializer, ProductsListSerializer, ProductRetrieveSerializer


class CategoryListApi(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @method_decorator(cache_page(3600))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProductsListByCategoryApi(ListAPIView):
    serializer_class = ProductsListSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']

        return get_products_by_category_slug(category_slug)

    @method_decorator(cache_page(3600))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProductRetrieveApi(RetrieveAPIView):
    serializer_class = ProductRetrieveSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        product_slug = self.kwargs['slug']
        return get_products_by_slug(product_slug)

    @method_decorator(cache_page(3600))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
