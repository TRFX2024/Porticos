# Generated by Django 5.0.3 on 2024-04-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_porticos', '0007_remove_alerta_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerta',
            name='visto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
