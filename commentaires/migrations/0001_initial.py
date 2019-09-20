# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\commentaires\migrations\0001_initial.py
# Size of source mod 2**32: 807 bytes
# Decompiled by https://python-decompiler.com
import datetime
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
     migrations.CreateModel(name='Commentaire',
       fields=[
      (
       'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'publication_id', models.CharField(max_length=100)),
      (
       'pseudo', models.CharField(max_length=100)),
      (
       'email', models.EmailField(max_length=254)),
      (
       'texte', models.TextField()),
      (
       'date_ajout', models.DateField(blank=True, default=(datetime.datetime.now)))])]