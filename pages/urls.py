# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\pages\urls.py
# Size of source mod 2**32: 190 bytes
# Decompiled by https://python-decompiler.com
from django.urls import path
from . import views
urlpatterns = [
 path('', (views.index), name='index'),
 path('about', views.about, name='about'),
 #path('agirencomplementarite', (views.agirencomp), name='agirencomp')
]