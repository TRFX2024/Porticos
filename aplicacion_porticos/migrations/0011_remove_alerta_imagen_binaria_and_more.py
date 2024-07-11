# Generated by Django 5.0.7 on 2024-07-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_porticos', '0010_fallo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerta',
            name='imagen_binaria',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='imagen_binaria',
        ),
        migrations.AddField(
            model_name='alerta',
            name='imagen',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='imagen',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]