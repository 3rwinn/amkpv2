# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\pages\views.py
# Size of source mod 2**32: 695 bytes
# Decompiled by https://python-decompiler.com
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from publications.models import Publication


def index(request):
    publications = Publication.objects.order_by(
        '-publication_date').filter(est_visible=True)
    context = {'publications': publications}
    return render(request, 'pages/accueil.html', context)


def agirencomp(request):
    publications_comp = Publication.objects.order_by(
        '-publication_date').filter(section_id=2, est_visible=True)
    context = {'publications': publications_comp}
    return render(request, 'pages/agirencomp.html', context)
 