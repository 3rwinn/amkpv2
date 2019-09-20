# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\comptes\views.py
# Size of source mod 2**32: 1561 bytes
# Decompiled by https://python-decompiler.com
from django.shortcuts import render, redirect
from .models import Comptes

def savecompte(request):
    if request.method == 'POST':
        nom_compte = request.POST['nom_compte']
        type_activite = request.POST['type_activite']
        sector_activite = request.POST['sector_activite']
        pays = request.POST['pays']
        slug = request.POST['slug']
        emetteur = request.POST['emetteur']
        logo = request.POST['logo']
        couleur = request.POST['couleur']
        mobile = request.POST['mobile']
        email = request.POST['email']
        siteweb = request.POST['siteweb']
        page_facebook = request.POST['page_facebook']
        page_instagram = request.POST['page_instagram']
        page_linkedin = request.POST['page_linkedin']
        page_youtube = request.POST['page_youtube']
        compte = Comptes(nom_compte=nom_compte, type_activite=type_activite, sector_activite=sector_activite, pays=pays,
          slug=slug,
          emetteur=emetteur,
          logo=logo,
          couleur=couleur,
          mobile=mobile,
          email=email,
          siteweb=siteweb,
          page_facebook=page_facebook,
          page_instagram=page_instagram,
          page_linkedin=page_linkedin,
          page_youtube=page_youtube)
        compte.save()
        return redirect('compte')
    else:
        compte = Comptes.objects.last()
        context = {'compte': compte}
        return render(request, 'comptes/index.html', context)