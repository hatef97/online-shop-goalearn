from django.contrib import admin

from .models import Product


@admin.register(Product)
class Postadmin(admin.ModelAdmin):
    list_display = ("user", "title", "price", "active", "datetime_created")
