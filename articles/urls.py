from django.urls import path
from . import views

urlpatterns = [
    path('vision', views.vision, name='vision'),
    path('', views.articles, name='articles'),
    path('<int:article_id>', views.article, name='article'),
]