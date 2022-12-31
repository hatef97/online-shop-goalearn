from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField


class Product(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = RichTextField(verbose_name=_("Description"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("Price"))
    active = models.BooleanField(default=True, verbose_name=_("Active"))
    cover = models.ImageField(upload_to='covers/', verbose_name=_("Cover"))
    product_quantity = models.PositiveIntegerField(default=0, verbose_name=_("Product quantity"))
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])
