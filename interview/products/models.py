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


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products-list-by-category', kwargs={'category_slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=150, db_index=True,)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE,
                                 related_name='category',
                                 )
    sales = models.ManyToManyField(Sale,
                                   related_name='sales',
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

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'category_slug': self.category.slug,
                                                 'slug': self.slug})

    def get_available_sales(self):
        return {sale.name: sale.percent for sale in self.sales.all()}
