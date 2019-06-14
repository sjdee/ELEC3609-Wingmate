from django.conf.urls import url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from . import views

from .models import WingmanLocation



urlpatterns = [
    url(r'^wingmap$', views.map, name ='wingmap'),
    url(r'^points.data', views.points_view, name='wingmanLocation'),
    url(r'^ajax/user_location/$', views.user_location, name="user_location"),
    url(r'^ajax/user_review/$', views.user_review, name="user_review")
]
