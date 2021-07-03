import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Product

context = {}


def index(request):
    products = Product.objects.all()
    return render(request, "ecommerce/index_page.html", context={"products": products})


def checkout_page(request):
    global context
    cart_context = context
    print(cart_context)
    return render(request,  "ecommerce/checkout_page.html", cart_context)


def checkout(request):
    global context
    if request.method == "POST":
        data = request.POST.getlist('items[]')
        context = {
            "products": [],
        }
        total_price = 0
        total_quantity = 0
        print(data)
        for item in data:
            id = item.split('-')[1].split('~')[0]
            quantity = item.split('-')[1].split('~')[1]
            print("id", id, "quantity", quantity)
            if int(quantity) >= 1:
                total_quantity += int(quantity)
                product = Product.objects.get(id=id)
                total_price += product.price * int(quantity)
                context["products"].append({
                    "name": product.name,
                    "quantity": quantity
                })
        context["total_price"] = total_price
        context["total_quantity"] = total_quantity
        print(context)
        return HttpResponse({"response": "ok"})


def load_products(request):
    Product.objects.all().delete()
    with open("ecommerce/resources/products.json", "r") as json_file:
        data = json.load(json_file)
        products = data["Products"]
        print(type(products))
        for product in products:
            print(product["name"], product["description"])
            Product.objects.create(
                name=product["name"],
                description=product["description"],
                price=product["price"],
                image=product["image"]
            )
    return JsonResponse({"response": "Ok. Products were loaded"})
