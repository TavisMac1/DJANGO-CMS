from django.db import models

from email.policy import default
from turtle import title
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
