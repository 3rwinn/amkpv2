# Generated by Django 2.2.4 on 2019-12-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20191215_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.CharField(choices=[('VISION', 'Vision'), ('ACTUALITES', 'Actualités')], default='', max_length=100),
        ),
    ]
