# Generated by Django 5.1.2 on 2024-10-29 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='dia_horario',
            field=models.TimeField(default='00:00'),
            preserve_default=False,
        ),
    ]
