from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_list, product_details

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("", product_list, name="product_list"),
    path("product/<int:pk>/", product_details, name="product_details")
]
