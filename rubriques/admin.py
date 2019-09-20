# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\rubriques\admin.py
# Size of source mod 2**32: 193 bytes
# Decompiled by https://python-decompiler.com
from django.contrib import admin
from .models import Rubrique

class RubriqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')


admin.site.register(Rubrique, RubriqueAdmin)