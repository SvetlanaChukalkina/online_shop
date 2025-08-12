from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Категория 1')

        products = [
            {'name': 'Продукт 1', 'description': 'Описание 1', 'category': category, 'price': 100},
            {'name': 'Продукт 2', 'description': 'Описание 2', 'category': category, 'price': 200},
            {'name': 'Продукт 3', 'description': 'Описание 3', 'category': category, 'price': 300},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.name}'))