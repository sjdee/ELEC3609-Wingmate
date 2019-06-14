# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.db.models import Q
from  django.core.exceptions import ObjectDoesNotExist

from wingmap.models import WingmanLocation
from myapp.models import WingmanUser, WingmanReview



@login_required(login_url='/login/')
def map(request):
    all_users = WingmanLocation.objects.all()
    context = {'users' : all_users }
    return render(request, 'wingmap/map.html', context)


# AJAX view that serves all the points as geojson files
# ideally would do a spatial search for all points in a given range
def points_view(request):
    points_as_geojson = serialize('geojson', WingmanLocation.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')


# AJAX view that sets the authenticated user's location
# additionally creates a WingmanLocation object if the location doesnt already exist
@login_required(login_url='/admin/login/')
def user_location(request):
    if request.method == 'GET':
        y = request.GET.get('lat')
        x = request.GET.get('long')
        data = {'lat' : x , 'long' : y}
        current_user = request.user
        print(current_user)
        print("this is x: ",  data, " for ", current_user.username)
        pnt = GEOSGeometry('{ "type": "Point", "coordinates": [ '+ x +', ' + y +' ] }') # GeoJSON
        try:
            location = WingmanLocation.objects.get(user=current_user)
            location.geom = pnt
            print location
        except ObjectDoesNotExist:
            location = WingmanLocation.objects.create(user=current_user,name=current_user.username, geom=pnt)
        location.save()
        return JsonResponse(data)



#An AJAX view that handles all the user review functionality
def user_review(request):
    #used for retriving the user's average rating, compiling all reviews
        #addionally updates the WingmanUser objects average rating
    if request.method == 'GET':
        username = request.GET.get('username')
        reviewee = WingmanUser.objects.get(user=User.objects.get(username=username))
        reviews = WingmanReview.objects.filter(reviewee=reviewee)
        avg_rating = average_rating(reviews)
        reviewee.averageRating = avg_rating;
        reviewee.save()
        canAcceess = canAccess(request.user, reviewee)
        return JsonResponse({'rating' : avg_rating, 'canAccess' : canAccess(request.user, reviewee), 'isCurrent' : isCurrent(request.user, username) })

    #used for updating the user rating
    elif request.method == 'POST':
        username = request.POST.get('username')
        rating = request.POST.get('rating')

        current_user = request.user.username
        reviewee = WingmanUser.objects.get(user=User.objects.get(username=username))
        reviewer = WingmanUser.objects.get(user=User.objects.get(username=current_user))

        try:
            review = WingmanReview.objects.get(reviewee=reviewee, reviewer=reviewer)
            review.rating = rating
            reviewee.averageRating = calulate_average_rating(reviewee)
        except WingmanReview.DoesNotExist:
            review = WingmanReview.objects.create(reviewee=reviewee, reviewer=reviewer, rating=rating)

        review.save() #atm can review yourself and can review someone you havent spoken too
        print(username + " rated " + rating)
        html = "<p class='indicator'>Hell yeah, you rated {0} {1} out of four.</p>".format(username, rating)
        return HttpResponse(html)


def calulate_average_rating(username):
    wuser =  WingmanUser.objects.get(user=(User.objects.get(username=username)))
    reviews = WingmanReview.objects.filter(reviewee=wuser)
    avg_rating = average_rating(reviews)
    return avg_rating

def average_rating(ratings):
    total = 0
    count = 0
    for r in ratings:
        total += r.rating
        count += 1

    if count == 0:
        return 0
    return total/(count)

#defines if the curren user can access the other wingmate
    #current user can access if other wingmate is under 3 stars
def canAccess(user, other_user):
    if (WingmanUser.objects.get(user=user).isPremium or other_user.averageRating <= 3):
         return True
    else:
        return False

def isCurrent(authenticated_user, username):
    if (authenticated_user.username == username):
        return True
    else:
        return False
