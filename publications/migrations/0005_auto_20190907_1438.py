# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\publications\migrations\0005_auto_20190907_1438.py
# Size of source mod 2**32: 616 bytes
# Decompiled by https://python-decompiler.com
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('publications', '0004_auto_20190825_1827')]
    operations = [
     migrations.AddField(model_name='publication',
       name='media_video_youtube',
       field=models.URLField(blank=True)),
     migrations.AlterField(model_name='publication',
       name='media_image',
       field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d/'))]