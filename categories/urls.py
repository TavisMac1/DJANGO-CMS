from django.contrib import admin
from django.urls import path
from . import views
app_name = 'categories'
urlpatterns = [
    path('categories/', views.category_list, name="list"),
    path('create/', views.create_category, name="create"),
    path('categories/<slug>', views.update_category, name="update"),
    path('delete/<slug>', views.delete_category, name="delete"),
]
