from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Product

# create collection from product model and serve it to the listing page for use
def public_list(request):
    products = Product.objects.all().order_by('date')
    return render(request, 'all_products.html', {'products': products})


def public_view(request, slug):
    products = Product.objects.get(slug=slug)
    return render(request, 'product_view.html', {'products': products})


def public_lookup(request, slug):
    products = Product.objects.all(category=slug)
    return render(request, 'product_lookup.html', {'products': products})
