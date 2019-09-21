# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\pages\views.py
# Size of source mod 2**32: 695 bytes
# Decompiled by https://python-decompiler.com
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from publications.models import Publication

import tweepy

# Authenticate to twitter
auth = tweepy.OAuthHandler("Cfa5MfJunGt68CesNSamX6CeA", 
    "Fo4WlqSe3jpw3cGwztQF0hejjVRYr0FbC3OMMp8tSkfV19O61Q")
auth.set_access_token("200647729-yEXnV9BcJr881gyUQ8uNOcOSmXROQYQy1vmScFGk", 
    "On8hwicGCgP30LvpWMtmSgOdowggsSOfhqWjYbFWvgCuW")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# Get last n tweets
tweets = api.user_timeline("amkpayne", count=9)


def index(request):
    publications = Publication.objects.order_by(
        '-publication_date').filter(est_visible=True)
    context = {'publications': publications, 'tweets': tweets}
    return render(request, 'pages/accueil.html', context)


def agirencomp(request):
    publications_comp = Publication.objects.order_by(
        '-publication_date').filter(section_id=2, est_visible=True)
    context = {'publications': publications_comp}
    return render(request, 'pages/agirencomp.html', context)
 