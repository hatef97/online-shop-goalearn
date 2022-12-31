from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(
        regex="^\+?[1-9][0-9]{7,14}$",
        message="Phone number must be entered in the format: "
                "'+999999999'. Up to 15 digits allowed."
    )

    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email"))
    first_name = models.CharField(max_length=250, verbose_name=_("First name"))
    last_name = models.CharField(max_length=250, verbose_name=_("Last name"))
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Age"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              null=True,
                              blank=True,
                              verbose_name=_("Gender"))
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=50,
                                    unique=True,
                                    verbose_name=_("Phone number"))
