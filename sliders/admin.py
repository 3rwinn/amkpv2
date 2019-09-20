# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\sliders\admin.py
# Size of source mod 2**32: 252 bytes
# Decompiled by https://python-decompiler.com
from django.contrib import admin
from .models import Slider

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre')
    list_display_links = ('id', 'titre')
    list_per_page = 25


admin.site.register(Slider, SliderAdmin)