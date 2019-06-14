from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^premium/$', views.index, name ='index'),
    url(r'^thankYou/$', views.thankYou, name ='thankYou'),
]
