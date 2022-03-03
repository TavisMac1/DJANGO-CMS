from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth.decorators import login_required
from . import forms


def category_list(request):
    cats = Category.objects.all().order_by('date')
    return render(request, 'categories_list.html', {'cats': cats})
