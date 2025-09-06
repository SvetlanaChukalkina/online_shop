from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def filter_product(category_id):
    filter_list = Product.objects.filter(category=category_id)
    return filter_list


def get_products_from_cache(queryset):
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
