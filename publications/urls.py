# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\urls.py
# Size of source mod 2**32: 349 bytes
# Decompiled by https://python-decompiler.com
from django.urls import path
from . import views
urlpatterns = [
 path('<int:section_id>/<int:rubrique_id>', (views.publications),
   name='publications'),
 path('<int:publication_id>', (views.publication), name='publication'),
 path('commentaire/<int:publication_id>', (views.commentaire),
   name='commentaire')]