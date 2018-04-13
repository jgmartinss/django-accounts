from django import forms

from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError

from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
    ReadOnlyPasswordHashField
)

from . import models


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(
        label='Email',

        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('email'),
                'required': True
            }
        )
    )

    username = forms.CharField(
        label="Username",

        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username',
                'required': 'true',
            }
        )
    )

    first_name = forms.CharField(
        label='First Name',

        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('first name'),
                'required': True
            }
        )
    )

    last_name = forms.CharField(
        label='Last Name',

        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('last name'),
                'required': True
            }
        )
    )

    password1 = forms.CharField(
        label='Password',

        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('password'),
                'required': True
            }
        )
    )

    password2 = forms.CharField(
        label='Password confirmation',

        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('password confirmation'),
                'required': True
            }
        )
    )

    gender = forms.ChoiceField(
        label='Gender',

        choices=models.GENDER_CHOICES,

        widget=forms.RadioSelect(
            attrs={
                'class': 'checkbox-inline'
            }
        )
    )

    class Meta:
        model = models.User

        fields = [
            'username', 'first_name', 'last_name', 'gender',
            'email', 'password1', 'password2'
        ]

        def clean_password(self):
            cleaned_data = self.cleaned_data
            if cleaned_data['password2'] != cleaned_data['password']:
                raise ValidationError('Password dont match')
            return cleaned_data['password2']


class LoginUserForm(AuthenticationForm):
    username = UsernameField(
        label='Email',

        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
                'placeholder': _('email')
            }
        ),
        error_messages={
            'required': _('Please enter your email'),
            'invalid': _('Please enter your email valid')
        },
    )

    password = forms.CharField(
        label='Password',

        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('password')
            }
        ),
        error_messages={
            'required': _('Please enter your password'),
            'invalid': _('Please enter your password valid')
        },
    )
