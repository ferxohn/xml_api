from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('name', )}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Client)
admin.site.register(models.CFDIIssued)
admin.site.register(models.CFDIReceived)
