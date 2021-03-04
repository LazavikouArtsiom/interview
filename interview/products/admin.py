from django.contrib import admin

from .models import (Product, Sale, Category,
                    Attribute, ProductAttribute, Manufacturer,
                    )

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sale)
admin.site.register(Attribute)
admin.site.register(ProductAttribute)
admin.site.register(Manufacturer)