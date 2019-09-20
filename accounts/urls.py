# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\accounts\urls.py
# Size of source mod 2**32: 432 bytes
# Decompiled by https://python-decompiler.com
from django.urls import path
from . import views
urlpatterns = [
 path('login', (views.login), name='login'),
 path('register', (views.register), name='register'),
 path('logout', (views.logout), name='logout'),
 path('dashboard', (views.dashboard), name='dashboard'),
 path('publications', (views.publications), name='publications'),
 path('add_publication', (views.add_publication), name='add_publication')]