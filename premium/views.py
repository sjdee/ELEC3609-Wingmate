# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as UserDjango
from myapp.models import WingmanUser


# Create your views here.
@login_required(login_url='/admin/login/')
def index(request):
	return render(request,'premium/buyPremium.html', context=None);

@login_required(login_url='/admin/login/')
def thankYou(request):
	print(request)
	currentUser = request.user # Get the logged in user
	currentWingmanUser = WingmanUser.objects.get(user=currentUser) # Get the associated wingmanuser
	currentWingmanUser.isPremium = True;
	currentWingmanUser.save()
	return render(request,'premium/thankYou.html', context=None);
