from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ContactsTemplateView, FilterListView,
                           HomeTemplateView, ProductCreateView,
                           ProductDeleteView, ProductDetailView,
                           ProductListView, ProductUnpublishView,
                           ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path(
        "product/<int:pk>/",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_details",
    ),
    path("product/create", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "product/<int:product_id>/unpublish/",
        ProductUnpublishView.as_view(),
        name="product_unpublish",
    ),
    path(
        "product/category/<int:category_id>/",
        FilterListView.as_view(),
        name="category_id",
    ),
]
