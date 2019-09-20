# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\rubriques\models.py
# Size of source mod 2**32: 160 bytes
# Decompiled by https://python-decompiler.com
from django.db import models


class Rubrique(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
