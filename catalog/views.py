from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from catalog.services import filter_product, get_products_from_cache


class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, template_name="catalog/contacts.html")


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset().filter(publication_status=True)
        return get_products_from_cache(queryset)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductUnpublishView(LoginRequiredMixin, View):
    model = Product
    form_class = ProductModeratorForm

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("Вы не можете отменить публикацию")
        product.publication_status = False
        product.save()
        return redirect("catalog:product_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        user = self.request.user
        product = super().get_object(queryset)
        if user == product.owner or user.has_perm("catalog.can_unpublish_product"):
            return product
        else:
            raise PermissionDenied


class FilterListView(ListView):
    model = Product
    template_name = "catalog/filter_list.html"

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return filter_product(category_id)
