from socket import fromshare
from django import forms
from . import models

class UpdateCategory(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['title']


class CreateCategory(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['title', 'slug']
