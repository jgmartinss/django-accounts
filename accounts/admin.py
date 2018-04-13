from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models
from . import forms


class UserAdmin(BaseUserAdmin):
    model = models.User

    radio_fields = {
        'gender': admin.HORIZONTAL
    }

    ordering = ('email', '-date_joined',)

    search_fields = ('email',)

    list_display = (
        'email', 'username', 'first_name', 'last_name', 'gender',
        'is_active', 'is_admin', 'is_superuser', 'date_joined'
    )

    list_display_links = ['email']

    list_filter = ('is_superuser', 'is_admin', 'is_active', 'date_joined')

    fieldsets = (
        ('Account info', {
            'fields': ('email', 'password', 'is_active')
        }),
        ('Personal info', {
            'fields': ('username', 'first_name', 'last_name', 'gender',)
        }),
        ('Permissions', {
            'fields': (('is_superuser', 'is_admin'),)
        }),
    )

    add_fieldsets = (
        ('Add user', {
            'classes': ('wide',),
            'fields': (
                'first_name',
                'last_name',
                'gender',
                'username',
                'email',
                'password1',
                'password2'
            )
        }),
    )

admin.site.register(models.User, UserAdmin)
