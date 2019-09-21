# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\migrations\0006_publication_type_de_media.py
# Size of source mod 2**32: 479 bytes
# Decompiled by https://python-decompiler.com
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('publications', '0005_auto_20190907_1438')]
    operations = [
     migrations.AddField(model_name='publication',
       name='type_de_media',
       field=models.CharField(choices=[('IMG', 'Image'), ('VID', 'Video')], default='IMG', max_length=3))]