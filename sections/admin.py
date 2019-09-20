# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\sections\admin.py
# Size of source mod 2**32: 188 bytes
# Decompiled by https://python-decompiler.com
from django.contrib import admin
from .models import Section

class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')


admin.site.register(Section, SectionAdmin)