from django.contrib import admin
from django.urls import path
from . import views
app_name = 'public'
urlpatterns = [
    path('list/', views.public_list, name="list"),
    path('list/<slug>', views.public_view, name="view"),
    path('lookup/<slug>', views.public_lookup, name="lookup"),
]
