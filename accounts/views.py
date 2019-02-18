from django.conf import settings

from django.http import Http404

from django.urls import reverse_lazy

from django.shortcuts import redirect

from django.utils.http import is_safe_url
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
    REDIRECT_FIELD_NAME,
    login as auth_login,
    logout as auth_logout,
)

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import RedirectView, FormView, TemplateView, CreateView

from . import forms


class RegisterView(SuccessMessageMixin, FormView):
    form_class = forms.RegisterUserForm
    template_name = 'register.html'
    success_message = _("@%(nickname)s, Account created successfully.")
    success_url = reverse_lazy('core:login')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data, nickname=cleaned_data['nickname']
        )

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            raise Http404(_('You are already logged in!'))
        return super(RegisterView, self).post(*args, **kwargs)

    def form_valid(self, form):
        user = form.save(False)
        user.save(True)
        return super(RegisterView, self).form_valid(form)


class LoginView(FormView):
    form_class = forms.LoginUserForm
    template_name = 'login.html'
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url = reverse_lazy('')

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        self.request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super(LoginView, self).get(*args, **kwargs)

    def form_valid(self, form):
        form = self.form_class(data=self.request.POST, request=self.request)

        if self.request.POST and form.is_valid():
            if not self.request.POST.get('remember_me', None):
                self.request.session.set_expiry(0)

            if self.request.session.test_cookie_worked():
                self.request.session.delete_test_cookie()

            auth_login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
        else:
            return self.render_to_response({'form': form})

    def get_success_url(self):
        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, allowed_hosts=[self.request.get_host()]):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(LoginRequiredMixin, RedirectView):
    url = ''

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        self.request.session.flush()
        return super(LogoutView, self).get(request, *args, **kwargs)
