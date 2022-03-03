from django.contrib import admin
from . models import Category #IMPORT THE CAT MODEL

admin.site.register(Category) #making the models feilds accessible by admin
