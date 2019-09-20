# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\admin.py
# Size of source mod 2**32: 445 bytes
# Decompiled by https://python-decompiler.com
from django.contrib import admin
from .models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'auteur', 'source', 'publication_date', 'est_visible')
    list_display_links = ('id', 'titre')
    list_filter = ('est_visible', )
    search_fileds = ('title', 'resume', 'auteur', 'source')
    list_per_page = 25


admin.site.register(Publication, PublicationAdmin)