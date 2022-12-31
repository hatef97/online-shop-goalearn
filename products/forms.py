from django.forms import ModelForm

from .models import Product


class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = ("title", "description", "price", "cover", "product_quantity", "active")
