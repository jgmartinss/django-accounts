import uuid

from django.db import models

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from . import managers


class MyUser(AbstractBaseUser,  PermissionsMixin):
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    nickname = models.CharField(_('Nickname'), max_length=50, unique=True)
    first_name = models.CharField(_('Firt Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)
    avatar = models.ImageField(
        _('Avatar'), null=True, blank=True, upload_to='image/avatar/'
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = managers.MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        app_label = 'accounts'

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
        return self.nickname

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.password:
            self.password = str(uuid.uuid4()).replace('-', '')
        super(MyUser, self).save(*args, **kwargs)
