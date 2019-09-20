# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\comptes\models.py
# Size of source mod 2**32: 919 bytes
# Decompiled by https://python-decompiler.com
from django.db import models

class Comptes(models.Model):
    nom_compte = models.CharField(max_length=200)
    type_activite = models.CharField(max_length=50)
    sector_activite = models.CharField(max_length=100)
    description_activite = models.TextField(blank=True)
    pays = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    emetteur = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    couleur = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    siteweb = models.CharField(max_length=100)
    page_facebook = models.URLField(max_length=100)
    page_instagram = models.URLField(max_length=100)
    page_linkedin = models.URLField(max_length=100)
    page_youtube = models.URLField(max_length=100)

    def __str__(self):
        return self.name