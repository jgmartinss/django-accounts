## Django Accounts CBV

A simple django authentication app using cbv, 


### Features already added

[x] Configure with django settings

[x] Custom User django

[x] Register, Login and Logout

### Features to be added

[ ] Email registration confirmation link

[ ] Password reset


### Start using django-accounts

1.  Install app in project:

    ```sh
    pip install git+https://github.com/jgmartinss/django-accounts-cbv
    ```

2.  Add `accounts` to `INSTALLED_APPS` in settings file:

    ```python
    # settings.py

    INSTALLED_APPS = (
       # ...
       'accounts',
    )
    ```

3.  Add these lines to your URL configuration, urls.py:

    ```python
    # urls.py

    urlpatterns = (
        # ...
        path('accounts/', include('accounts.urls')),
    )
    ```

4.  Create your or edit User template if desired:

    ```python
    # models.py

    class User(AbstractBaseUser,  PermissionsMixin):
        email = models.EmailField(_('Email'), max_length=255, unique=True)
        nickname = models.CharField(_('Nickname'), max_length=120, unique=True)
        first_name = models.CharField(_('Firt Name'), max_length=255)
        last_name = models.CharField(_('Last Name'), max_length=255)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        is_admin = models.BooleanField(default=False)
    ```

5.  Add URL path in success_url in LoginView:

    ```python
    # models.py

    class LoginView(FormView):
        success_url = reverse_lazy('EXEMPLE:EXEMPLE')
    ```

6.  Configure django-accounts-cbv in your settings:

    ```python
    # settings.py

    AUTH_USER_MODEL = 'accounts.User'

    AUTHENTICATION_BACKENDS = (
        ('django.contrib.auth.backends.ModelBackend'),
    )
    ```

7.  Run the app and check it out:

    ```shell
    $ python manage.py makemigrations accounts
    $ python manage.py migrate
    $ python manage.py runserver
    $ python manage.py createsuperuser
    ```
