from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('a_crosswalk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crosswalk',
            name='instt_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
