from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	# url(r'^register/$', views.register, name='register'),
	# url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout-redirect$', views.logout_redirect, name='logout_redirect'),
]
