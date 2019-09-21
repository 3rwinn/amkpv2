# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\migrations\0001_initial.py
# Size of source mod 2**32: 1209 bytes
# Decompiled by https://python-decompiler.com
import datetime
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
     migrations.CreateModel(name='Publication',
       fields=[
      (
       'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'section', models.CharField(max_length=100)),
      (
       'rubrique', models.CharField(max_length=100)),
      (
       'titre', models.CharField(max_length=200)),
      (
       'resume', models.TextField(blank=True)),
      (
       'texte', models.TextField()),
      (
       'media_image', models.ImageField(upload_to='media/%Y/%m/%d/')),
      (
       'mots_cles', models.CharField(max_length=300)),
      (
       'auteur', models.CharField(max_length=100)),
      (
       'source', models.CharField(max_length=100)),
      (
       'publication_date', models.DateField(blank=True, default=(datetime.datetime.now))),
      (
       'est_visible', models.BooleanField(default=True))])]