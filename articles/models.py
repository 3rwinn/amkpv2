from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    VISION = 'VISION'
    ACTUALITES = 'ACTUALITES'
    CATEGORIES = [
        (VISION, 'Vision'),
        (ACTUALITES, 'Actualités')
    ]

    titre = models.CharField(max_length=200)
    categorie = models.CharField(max_length=100,choices=CATEGORIES, default='')
    image_principale = models.ImageField(upload_to='media/articles/%Y/%m/%d/')
    texte = models.TextField()
    date_publication = models.DateField(default=datetime.now, blank=True)
    est_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre
