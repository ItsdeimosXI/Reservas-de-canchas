# Generated by Django 5.1.2 on 2024-11-12 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Canchas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=48)),
                ('numero_cancha', models.IntegerField()),
                ('descripcion', models.TextField(max_length=1086)),
                ('lugar', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='canchas.lugar')),
            ],
        ),
    ]
