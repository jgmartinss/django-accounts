from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('accounts/signin/', views.SignInView.as_view(), name='sign-in'),
	path('accounts/signup/', views.SignUpView.as_view(), name='sign-up'),
	path('accounts/signup/done/', views.SignUpDoneView.as_view(), name='sign-up-done'),
	path('logout/', views.LogoutView.as_view(), name='logout'),

]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
						  document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
						  document_root=settings.MEDIA_ROOT)
