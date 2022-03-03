from socket import fromshare
from django import forms
from . import models

class UpdateProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['category','title','description','price','quantity','sku','picture']


class CreateProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['category','title','description','price','quantity','sku','picture','slug']