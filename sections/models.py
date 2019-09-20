# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\sections\models.py
# Size of source mod 2**32: 236 bytes
# Decompiled by https://python-decompiler.com
from django.db import models

class Section(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.nom