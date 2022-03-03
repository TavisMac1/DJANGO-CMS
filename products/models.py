from django.db import models

from email.policy import default
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from categories import models as categories

class Product(models.Model):
    # make the field unique
    category = models.ForeignKey(categories.Category, default=None, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.BigIntegerField()
    sku = models.BigIntegerField()
    picture = models.ImageField(default="default.png", blank=True)
    # a slug to use as an identifier when editing and deleting
    slug = models.SlugField(default=None, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
