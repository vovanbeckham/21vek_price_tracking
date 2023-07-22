from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import json

from price_21vek.models import Catalog, Category, Product


def index(request):
    catalog = Catalog.objects.all()
    context = {
        'catalog': catalog,
    }
    return render(request, 'price_21vek/index.html', context=context)

def catalogy(request, catalog_slug):
    #catalogs = get_object_or_404(Catalog, slug=catalog_slug)
    catalog = Catalog.objects.all()
    for cat in catalog:
        if cat.slug==catalog_slug:
            categoryes = cat.category_set.all()
            break
    #print(categoryes)
    print(catalog)
    context = {
        'title': catalog.get(slug=catalog_slug),
        'catalog': catalog,
        'categoryes': categoryes,
    }
    print('ok_cat')
    return render(request, 'price_21vek/category.html', context=context)



def product_price(request, product_slug):
    print('ok price')
    print(product_slug)
    catalog = Catalog.objects.all()
    products = Category.objects.get(slug=product_slug).product_set.all()
    print(products)
    print(f'catalog = {catalog}')
    context = {
        'title': product_slug,
        'catalog': catalog,
        'products': products,
    }
    print('ok')
    return render(request, 'price_21vek/product_price.html', context=context)


def updates(request):
    print("ok")


    with open("data_test/electronics/electronics.json", "r") as file:
        json_string = file.read()
        parsed_json = json.loads(json_string)
    for js in parsed_json:
#        print(js["name"])
        Category.objects.create(name=js["name"],
                                url_categories=js["url"],
                                slug=js["url_slug"],
                                catalogs_id=2
                                )
        print(f"add {js['name']}")

    return HttpResponse("Страница приложения updates.")