from django.shortcuts import get_object_or_404, render
from .models import Article
from django.template.loader_tags import register


# Create your views here.
def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article
    }
    return render(request, 'articles/article.html', context)


def articles(request):
    articles = Article.objects.order_by('-date_publication').filter(est_visible=True, categorie='ACTUALITES')

    context = {
        'articles': articles
    }
    return render(request, 'articles/articles.html', context)

@register.inclusion_tag('articles/recent_articles.html')
def recent_articles():
    recent_articles = Article.objects.order_by('-date_publication')[:2]
    return {'recent_articles': recent_articles}


def vision(request):
    articles = Article.objects.order_by('-date_publication').filter(est_visible=True, categorie='VISION')

    context = {
        'articles': articles
    }
    return render(request, 'articles/articles.html', context)