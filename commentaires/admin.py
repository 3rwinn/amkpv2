# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\commentaires\admin.py
# Size of source mod 2**32: 249 bytes
# Decompiled by https://python-decompiler.com
from django.contrib import admin
from .models import Commentaire


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'pseudo', 'email', 'texte')
    list_per_page = 25


admin.site.register(Commentaire, CommentaireAdmin)
