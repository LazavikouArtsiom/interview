from rest_framework import serializers

from products.models import (Category, Product, Sale,
                             )
import django_filters


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'url']


class ProductsListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    sales = serializers.DictField(source='get_available_sales')
    total_price = serializers.SerializerMethodField()
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Product
        fields = ['slug', 'name', 'price',
                  'category', 'total_price', 'sales',
                  'id', 'url',
                  ]
        read_only_fields = ('price', 'slug')

    def get_total_price(self, obj):
        return obj.calculate_price_with_sale()


class ProductCreateSerializer(serializers.ModelSerializer):
    """
        Using in CartItemCreateSerializer for adding
        product in cart
    """
    class Meta:
        model = Product
        fields = ['slug']


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    total_price = serializers.SerializerMethodField()
    sales = serializers.CharField(source='get_available_sales')

    class Meta:
        model = Product
        fields = ['slug', 'name', 'price',
                  'category', 'total_price', 'sales',
                  'id',
                  ]
        lookup_field = 'slug'
        read_only_fields = ('price', 'slug')

    def get_total_price(self, obj):
        return obj.calculate_price_with_sale()
