from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
     ('publications', '0001_initial')]
    operations = [
     migrations.AlterField(model_name='publication',
       name='section',
       field=models.ForeignKey(on_delete=(django.db.models.deletion.DO_NOTHING), to='sections.Section'))]