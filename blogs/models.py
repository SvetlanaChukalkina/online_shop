from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=250, verbose_name="Заголовок статьи")
    body = models.TextField(verbose_name="Текст статьи")
    preview = models.ImageField(
        upload_to="blogs/blog/photo", blank=True, null=True, verbose_name="Превью"
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    count_of_view = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["created_at"]

    def __str__(self):
        return self.name
