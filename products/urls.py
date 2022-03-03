from django.contrib import admin
from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('list/', views.product_list, name="list"),
    path('make-product/', views.create_product, name="create"),
    path('create-product/<slug>', views.update_product, name="update"),
    path('delete-product/<slug>', views.delete_product, name="delete"),
]
