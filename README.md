# Django Accounts

A simple application for custom authentication in django, 
Enable your users to log in easily, log out, register and manage your profile.


## Features already added

[x] Configure with django settings

[x] Custom User django

[x] Register, Login and Logout

## Features to be added

[ ] Email registration confirmation link

[ ] Password reset


## Start using django-accounts

1.  Add `accounts` to `INSTALLED_APPS` in settings file:

    ```python
    # settings.py

    INSTALLED_APPS = (
       # ...
       'accounts',
    )
    ```

1.  Add these lines to your URL configuration, urls.py:

    ```python
    # urls.py

    urlpatterns = (
        # ...
        path('', include('accounts.urls')),
    )
    ```

1.  Create your or edit User template if desired:

    ```python
    # models.py

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
    ```

1.  Configure django-accounts in your settings:

    ```python
    # settings.py

    AUTH_USER_MODEL = 'accounts.MyUser'

    AUTHENTICATION_BACKENDS = (
        ('django.contrib.auth.backends.ModelBackend'),
    )

    STATIC_URL = '/static/'
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

1.  Run the app and check it out:

    ```shell
    $ python manage.py makemigrations accounts
    $ python manage.py migrate
    $ python manage.py runserver
    $ python manage.py createsuperuser
    ```
