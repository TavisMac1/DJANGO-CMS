from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from . import crud

def product_list(request):
    products = Product.objects.all().order_by('date')
    return render(request, 'product_list.html', {'products': products})


def create_product(request):
    if request.method == "POST":
        #if post from create form, then make the article with form values, else redirect back
        product = crud.CreateProduct(request.POST, request.FILES)
        if product.is_valid():
            newProduct = product.save(commit=False)
            newProduct.save()
            return redirect('products:list')
    else:
        product = crud.CreateProduct(request.POST)
    return render(request, 'create_product.html', {'product': product})


def update_product(request, slug):
    product = Product.objects.get(slug=slug)
    form = form.UpdateProduct(request.POST, instance=prod)
    if form.is_valid():
        form.save()
        return redirect('products:list')
    return render(request, 'update_product.html', {'product': product, 'form': form})


def delete_product(request, slug):
    product = Product.objects.get(slug=slug)
    product.delete()
    return redirect('products:list')
