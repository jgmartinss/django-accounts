import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from . import managers


GENDER_CHOICES = (
    (1, _('Male')),
    (2, _('Female')),
)


class User(AbstractBaseUser,  PermissionsMixin):
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    username = models.CharField(_('Username'), max_length=120, unique=True)
    first_name = models.CharField(_('Firt Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)
    gender = models.IntegerField(
        _('Gender'), choices=GENDER_CHOICES, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        app_label = 'accounts'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_tablespace = 'tb_user'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def get_nickname(self):
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.password:
            self.password = str(uuid.uuid4()).replace('-', '')
        super(User, self).save(*args, **kwargs)
