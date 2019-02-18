from django import forms

from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError

from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
)

from . import models


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(
        label=_('Email'),
        widget=forms.EmailInput(
            attrs={"class": 'form-control', 'placeholder': _('Email'), 'required': True}
        ),
    )

    nickname = forms.RegexField(
        label='Nickname',
        max_length=50,
        regex=r'^[\w.@+-]+$',
        help_text=_(
            'Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'
        ),
        error_messages={
            'invalid': _(
                'This value may contain only letters, numbers and @/./+/-/_ characters.'
            )
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'nickname',
                'required': 'true',
            }
        ),
    )

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('password'),
                'required': True,
            }
        ),
    )

    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('password confirmation'),
                'required': True,
            }
        ),
    )

    class Meta:
        model = models.User

        fields = [
            'email',
            'nickname',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

        def clean_password(self):
            cleaned_data = self.cleaned_data
            if cleaned_data['password2'] != cleaned_data['password']:
                raise ValidationError(_('Password dont match'))
            return cleaned_data['password2']


class LoginUserForm(AuthenticationForm):
    username = UsernameField(
        label=_('Email'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
                'placeholder': _('email'),
            }
        ),
        error_messages={
            'required': _('Please enter your email'),
            'invalid': _('Please enter your email valid'),
        },
    )

    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': _('password')}
        ),
        error_messages={
            'required': _('Please enter your password'),
            'invalid': _('Please enter your password valid'),
        },
    )

    remember_me = forms.BooleanField(label=_('Remember Me'), required=False)
