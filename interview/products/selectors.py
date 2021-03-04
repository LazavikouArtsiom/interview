from .models import Product


def get_products_by_category_slug(category_slug: str):
    return Product.objects.filter(category__slug=category_slug)


def get_products_by_slug(slug: str):
    return Product.objects.filter(slug=slug)
