# Generated by Django 5.0.3 on 2024-04-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_porticos', '0008_alerta_visto'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerta',
            name='imagen_binaria',
            field=models.TextField(blank=True, null=True),
        ),
    ]