from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, template_name="catalog/contacts.html")


def product_list(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, 'product_list.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product" : product}
    return render(request, 'product_details.html', context)
