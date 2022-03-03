from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth.decorators import login_required
from . import create


def category_list(request):
    cats = Category.objects.all().order_by('date')
    return render(request, 'categories_list.html', {'cats': cats})

def create_category(request):
    if request.method == "POST":
        #if post from create form, then make the article with form values, else redirect back
        cat = create.CreateCategory(request.POST)
        if cat.is_valid():
            newCategory = cat.save(commit=False)
            newCategory.save()
            return redirect('categories:list')
    else:
        cat = create.CreateCategory(request.POST)
    return render(request, 'create_category.html', {'cat':cat})

def update_category(request, slug):
    cat = Category.objects.get(slug=slug)
    form = create.UpdateCategory(request.POST, instance=cat)
    if form.is_valid():
        form.save()
        return redirect('categories:list')
    return render(request, 'update_category.html', {'cat':cat, 'form':form})


def delete_category(request, slug):
    cat = Category.objects.get(slug=slug)
    cat.delete()
    return redirect('categories:list')
