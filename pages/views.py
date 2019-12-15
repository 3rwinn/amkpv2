from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from articles.models import Article
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

import tweepy

# Authenticate to twitter
'''auth = tweepy.OAuthHandler("Cfa5MfJunGt68CesNSamX6CeA", 
    "Fo4WlqSe3jpw3cGwztQF0hejjVRYr0FbC3OMMp8tSkfV19O61Q")
auth.set_access_token("200647729-yEXnV9BcJr881gyUQ8uNOcOSmXROQYQy1vmScFGk", 
    "On8hwicGCgP30LvpWMtmSgOdowggsSOfhqWjYbFWvgCuW")'''

# Create API object
#api = tweepy.API(auth, wait_on_rate_limit=True,
#    wait_on_rate_limit_notify=True)

# Get last n tweets
#tweets = api.user_timeline("amkpayne", count=9)


def index(request):
    articles = Article.objects.order_by('-date_publication').filter(est_visible=True)
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles
    }
    return render(request, 'pages/accueil.html', context)

def about(request):
    return render(request, 'pages/about.html')




 