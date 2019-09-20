# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\contacts\migrations\0001_initial.py
# Size of source mod 2**32: 696 bytes
# Decompiled by https://python-decompiler.com
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
     migrations.CreateModel(name='Contact',
       fields=[
      (
       'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'nom_complet', models.CharField(max_length=200)),
      (
       'adresse_email', models.EmailField(max_length=254)),
      (
       'sujet', models.CharField(max_length=200)),
      (
       'texte', models.TextField())])]