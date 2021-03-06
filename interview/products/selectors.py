from .models import Product


def get_products_by_category_slug(category_slug: str):
    return Product.objects.select_related('category').prefetch_related('sales').filter(category__slug=category_slug)


def get_products_by_slug(slug: str):
    return Product.objects.select_related('category').prefetch_related('sales').filter(slug=slug)
