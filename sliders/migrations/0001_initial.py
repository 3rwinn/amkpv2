# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\sliders\migrations\0001_initial.py
# Size of source mod 2**32: 584 bytes
# Decompiled by https://python-decompiler.com
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
     migrations.CreateModel(name='Slider',
       fields=[
      (
       'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'titre', models.CharField(max_length=200)),
      (
       'image', models.ImageField(upload_to='media/%Y/%m/%d/'))])]