# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User


class WingmanLocation(models.Model):
    #user = models.ForeignKey('auth.User',default=User.objects.get(username='chris'))
    #this needs to have a refrence to the user it is using
    #  user = models.OneToManyField(User, default=User.objects.get(pk=default).id);
    name = models.CharField('name', max_length=100);
    user = models.OneToOneField(User)
    geom = gismodels.PointField(default=Point(0,0));
    objects = gismodels.GeoManager();

    def __str__(self):
        return self.name;

    def __unicode__(self):
        return self.name



class Wingman(models.Model):
    user = models.OneToOneField(User)
