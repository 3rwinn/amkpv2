# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\sections\migrations\0002_section_slug.py
# Size of source mod 2**32: 494 bytes
# Decompiled by https://python-decompiler.com
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('sections', '0001_initial')]
    operations = [
        migrations.AddField(model_name='section',
                            name='slug',
                            field=models.CharField(
                                default=(django.utils.timezone.now), max_length=100),
                            preserve_default=False)]
