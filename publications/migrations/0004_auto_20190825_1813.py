# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\migrations\0004_auto_20190825_1813.py
# Size of source mod 2**32: 506 bytes
# Decompiled by https://python-decompiler.com
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
     ('publications', '0003_auto_20190825_1812')]
    operations = [
     migrations.AlterField(model_name='publication',
       name='section',
       field=models.ForeignKey(on_delete=(django.db.models.deletion.DO_NOTHING), to='sections.Section'))]