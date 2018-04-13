from django.utils.http import is_safe_url
from django.utils.decorators import method_decorator

from django.urls import reverse_lazy

from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters

from django.views import generic

from . import forms
from . import models


class IndexView(generic.TemplateView):
    template_name = 'accounts/index.html'


class SignUpView(generic.CreateView):
    model = models.User
    form_class = forms.RegisterUserForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('sign-up-done')


class SignUpDoneView(generic.TemplateView):
    template_name = 'accounts/sign_up_done.html'


class SignInView(generic.FormView):
    form_class = forms.LoginUserForm
    template_name = 'accounts/sign_in.html'
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url = reverse_lazy('index')

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        
        return super(SignInView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(SignInView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(LoginRequiredMixin, generic.RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

