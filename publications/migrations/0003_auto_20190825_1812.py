# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\migrations\0003_auto_20190825_1812.py
# Size of source mod 2**32: 416 bytes
# Decompiled by https://python-decompiler.com
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('publications', '0002_auto_20190825_1809')]
    operations = [
     migrations.AlterField(model_name='publication',
       name='section',
       field=models.CharField(max_length=100))]