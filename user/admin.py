"""
Django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from user import models


class UserAdmin(BaseUserAdmin):
    """ Define the admin pages for users """
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name', 'last_login', 'id']
    search_fields = ['email', 'id']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'),
         {'fields': ('first_name', 'last_name', 'gender', 'phone_number',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'gender',
                'phone_number',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


admin.site.register(models.User, UserAdmin)