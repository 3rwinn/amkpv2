# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\views.py
# Size of source mod 2**32: 1639 bytes
# Decompiled by https://python-decompiler.com
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Publication
from commentaires.models import Commentaire

def publications(request, section_id, rubrique_id):
    publications = Publication.objects.order_by('-publication_date').filter(section_id=section_id, rubrique_id=rubrique_id)
    context = {'publications': publications}
    return render(request, 'pages/publications.html', context)


def publication(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    commentaires = Commentaire.objects.order_by('-date_ajout').filter(publication_id=publication_id)
    context = {'publication':publication, 
     'commentaires':commentaires}
    return render(request, 'pages/publication.html', context)


def commentaire(request, publication_id):
    if request.method == 'POST':
        publication_id = request.POST['publication_id']
        pseudo = request.POST['pseudo']
        email = request.POST['email']
        texte = request.POST['texte']
        commentaire = Commentaire(publication_id=publication_id,
          pseudo=pseudo,
          email=email,
          texte=texte)
        commentaire.save()
        messages.success(request, 'Votre a bien été enregistré')
        return redirect('/publications/' + publication_id)