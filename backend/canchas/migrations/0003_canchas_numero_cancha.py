# Generated by Django 5.1.2 on 2024-10-29 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0002_alter_canchas_descripcion_alter_canchas_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='canchas',
            name='numero_cancha',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
