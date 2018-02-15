from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from . import models
from . import forms


@admin.register(models.MyUser)
class UserAdmin(BaseUserAdmin):
    model = models.MyUser

    form = forms.UserChangeForm

    add_form = forms.RegisterUserForm

    ordering = ('email', '-date_joined',)

    search_fields = ('email',)

    list_display = (
        'email', 'nickname', 'first_name', 'last_name', 'is_active', 'date_joined'
    )

    #list_editable = ['first_name', 'last_name']

    list_display_links = ['email']

    list_filter = ('is_superuser', 'is_admin', 'is_active', 'date_joined')

    filter_horizontal = ()

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('nickname', 'first_name', 'last_name', 'avatar',)
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_admin', 'is_active')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'avatar', 'password1', 'password2')
        }),
    )
