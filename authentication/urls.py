from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
import django

from django.contrib import admin


urlpatterns = [
	url(r'^signup/$', views.user_signup, name='signup'),
	# url(r'^login/$', auth_views.login, name='login'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.logout_user, name='logout'),
	url(r'^logout-redirect$', views.logout_redirect, name='logout_redirect'),
]
