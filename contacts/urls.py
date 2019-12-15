# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\contacts\urls.py
# Size of source mod 2**32: 126 bytes
# Decompiled by https://python-decompiler.com
from django.urls import path
from . import views
urlpatterns = [
 path('', views.contact, name='contact')
]