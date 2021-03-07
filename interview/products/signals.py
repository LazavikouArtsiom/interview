from .services import calculate_price_with_sales


def calculate_price_for_product_with_new_set_of_sales(sender, instance, **kwargs):
    price_with_sales = calculate_price_with_sales(product=instance)
    instance.price_with_sales = price_with_sales
    instance.save()
