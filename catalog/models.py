from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта")
    photo = models.ImageField(
        upload_to="catalog/product/photo",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    price = models.IntegerField(verbose_name="Стоимость продукта")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего изменения", auto_now=True
    )
    publication_status = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["price", "category", "name"]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product')
        ]

    def __str__(self):
        return self.name
