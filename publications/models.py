# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\models.py
# Size of source mod 2**32: 1283 bytes
# Decompiled by https://python-decompiler.com
from django.db import models
from datetime import datetime
from sections.models import Section
from rubriques.models import Rubrique
from sources.models import Source


class Publication(models.Model):
    IMAGE = 'IMG'
    VIDEO = 'VID'
    TYPE_MEDIA = [
        (
            IMAGE, 'Image'),
        (
            VIDEO, 'Video Youtube')]
    section = models.ForeignKey(Section, on_delete=(models.DO_NOTHING))
    rubrique = models.ForeignKey(Rubrique, on_delete=(models.DO_NOTHING))
    titre = models.CharField(max_length=200)
    resume = models.TextField(blank=True)
    texte = models.TextField(blank=False)
    type_de_media = models.CharField(max_length=3,
                                     choices=TYPE_MEDIA,
                                     default=IMAGE)
    media_image = models.ImageField(upload_to='media/%Y/%m/%d/',
                                    blank=True,
                                    null=True,
                                    default='/static/media/default.png')
    media_video_youtube = models.URLField(blank=True)
    mots_cles = models.CharField(max_length=300)
    auteur = models.CharField(max_length=100)
    source = models.ForeignKey(Source, on_delete=(models.DO_NOTHING))
    publication_date = models.DateField(default=(datetime.now), blank=True)
    est_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre
