# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\sources\models.py
# Size of source mod 2**32: 158 bytes
# Decompiled by https://python-decompiler.com
from django.db import models

class Source(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom