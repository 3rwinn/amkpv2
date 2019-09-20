# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\contacts\models.py
# Size of source mod 2**32: 326 bytes
# Decompiled by https://python-decompiler.com
from django.db import models

class Contact(models.Model):
    nom_complet = models.CharField(max_length=200)
    adresse_email = models.EmailField()
    sujet = models.CharField(max_length=200)
    texte = models.TextField()

    def __str__(self):
        return self.adresse_email