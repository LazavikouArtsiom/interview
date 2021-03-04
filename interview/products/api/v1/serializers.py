from rest_framework import serializers

from products.models import (Category, Product, Sale,
                             Attribute,
                             )
import django_filters

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['name', 'percent']


class FilterCategorySerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = Category
        fields = ['name', 'children']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    sales = SaleSerializer(read_only=True, many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['slug', 'name', 'price',
                  'category', 'total_price', 'sales',
                  ]
    
    def get_total_price(self, obj):
        return obj.calculate_price_with_sale()


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    total_price = serializers.SerializerMethodField()
    sales = SaleSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['slug', 'name', 'price',
                  'category', 'total_price', 'sales',
                  ]
        lookup_field = 'slug'

    def get_total_price(self, obj):
        return obj.calculate_price_with_sale()