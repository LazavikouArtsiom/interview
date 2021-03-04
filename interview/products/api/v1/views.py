from rest_framework.generics import ListAPIView, RetrieveAPIView

from products.models import Category, Product
from products.selectors import get_products_by_category_slug, get_products_by_slug
from .serializers import CategorySerializer, ProductListSerializer, ProductRetrieveSerializer

class CategoryListApi(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsListByCategoryApi(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']

        return get_products_by_category_slug(category_slug)


class ProductRetrieveApi(RetrieveAPIView):
    serializer_class = ProductRetrieveSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        product_slug = self.kwargs['slug']
        return get_products_by_slug(product_slug)