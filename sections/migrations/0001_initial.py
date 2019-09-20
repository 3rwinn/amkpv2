# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\sections\migrations\0001_initial.py
# Size of source mod 2**32: 507 bytes
# Decompiled by https://python-decompiler.com
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name='Section',
                               fields=[
                                   (
                                    'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                                   (
                                       'nom', models.CharField(max_length=100))])]
