from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blogs.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(is_active="True")


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_view += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("name", "body", "preview", "is_active")
    success_url = reverse_lazy("blogs:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("name", "body", "preview", "is_active")

    def get_success_url(self):
        return reverse_lazy("blogs:blog_detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")
