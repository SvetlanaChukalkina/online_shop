from django.contrib import admin
from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "count_of_view")
    list_filter = ("created_at",)
    search_fields = ("name", "body")
