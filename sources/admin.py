# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\sources\admin.py
# Size of source mod 2**32: 179 bytes
# Decompiled by https://python-decompiler.com
from django.contrib import admin
from .models import Source

class SourceAdmin(admin.ModelAdmin):
    list_display = ('nom', )


admin.site.register(Source, SourceAdmin)