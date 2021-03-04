from datetime import timedelta

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.timezone import now


class Sale(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    percent = models.IntegerField()

    class Meta:
        ordering = ('name', 'percent')
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=255, null=True, blank=True)
    country = models.CharField(
        max_length=150, null=True, blank=True)

    class Meta:
        ordering = ('name', 'country')

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               verbose_name='Категория-родитель',
                               related_name='children'
                               )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, db_index=True,
                            verbose_name='Название')
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена')
    category = models.ForeignKey(Category,
                                 related_name='category',
                                 null=True,
                                 blank=True,
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE,
                                 )
    sales = models.ManyToManyField(Sale, 
                                   related_name='sales',
                                   verbose_name='Скидка',
                                   blank=True
                                   )
    class Meta:
        ordering = ('name',)
        index_together = ('id', 'slug')
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}'

    def calculate_price_with_sale(self) -> float:
        sales_percent = sum([sale.percent for sale in self.sales.all()])
        return float(self.price) - (float(self.price) * (0.01 * sales_percent))


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute,
                                  null=True,
                                  on_delete=models.SET_NULL)
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Product attribute'

    def __str__(self):
        return f'{self.product.name} | {self.attribute.name} | {self.value}'
