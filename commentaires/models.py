# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\commentaires\models.py
# Size of source mod 2**32: 390 bytes
# Decompiled by https://python-decompiler.com
from django.db import models
from datetime import datetime

class Commentaire(models.Model):
    publication_id = models.CharField(max_length=100)
    pseudo = models.CharField(max_length=100)
    email = models.EmailField()
    texte = models.TextField()
    date_ajout = models.DateField(default=(datetime.now), blank=True)

    def ___str___(self):
        return self.email