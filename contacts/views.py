# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\contacts\views.py
# Size of source mod 2**32: 651 bytes
# Decompiled by https://python-decompiler.com
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        nom_complet = request.POST['nom_complet']
        adresse_email = request.POST['adresse_email']
        sujet = request.POST['sujet']
        texte = request.POST['texte']
        contact = Contact(nom_complet=nom_complet, adresse_email=adresse_email,
                          sujet=sujet,
                          texte=texte)
        contact.save()
        messages.success(
            request, 'Votre demande de contact a bien été envoyé.')
        return redirect('/')
