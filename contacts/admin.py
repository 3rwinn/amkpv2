# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\contacts\admin.py
# Size of source mod 2**32: 276 bytes
# Decompiled by https://python-decompiler.com
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_complet', 'adresse_email', 'sujet')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)