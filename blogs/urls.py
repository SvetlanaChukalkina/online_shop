from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = BlogsConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/blog_create/", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/<int:pk>/blog_update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blogs/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
