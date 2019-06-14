from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^about/$', views.about, name='about'),
	url(r'^posts/$', views.posts, name='posts'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^accounts/profile/$', views.profile, name='profile'),
]
