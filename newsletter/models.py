from django.db import models
from datetime import datetime

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    date_inscription = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email