# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\migrations\0002_auto_20190825_1815.py
# Size of source mod 2**32: 495 bytes
# Decompiled by https://python-decompiler.com
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
     ('publications', '0001_initial')]
    operations = [
     migrations.AlterField(model_name='publication',
       name='section',
       field=models.ForeignKey(on_delete=(django.db.models.deletion.DO_NOTHING), to='sections.Section'))]