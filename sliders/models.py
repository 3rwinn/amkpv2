# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\sliders\models.py
# Size of source mod 2**32: 253 bytes
# Decompiled by https://python-decompiler.com
from django.db import models

class Slider(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/%Y/%m/%d/')

    def ___str__(self):
        return self.titre