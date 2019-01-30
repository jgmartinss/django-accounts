from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models


class UserAdmin(BaseUserAdmin):
    model = models.User
    ordering = ('email', '-created_at')
    search_fields = ('email',)
    list_display = (
        'email',
        'nickname',
        'first_name',
        'last_name',
        'is_active',
        'is_admin',
        'is_superuser',
        'created_at',
    )
    list_display_links = ['email']
    list_filter = ('is_superuser', 'is_admin', 'is_active', 'created_at')
    fieldsets = (
        ('Account info', {'fields': ('email', 'password', 'is_active')}),
        ('Personal info', {'fields': ('nickname', 'first_name', 'last_name')}),
        ('Permissions', {'fields': (('is_superuser', 'is_admin'),)}),
    )
    add_fieldsets = (
        (
            'Add user',
            {
                'classes': ('wide',),
                'fields': (
                    'first_name',
                    'last_name',
                    'nickname',
                    'email',
                    'password1',
                    'password2',
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
