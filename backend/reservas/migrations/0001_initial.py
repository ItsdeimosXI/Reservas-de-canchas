# Generated by Django 5.1.2 on 2024-11-12 19:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('canchas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('horario', models.TimeField()),
                ('cancha_reservada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.canchas')),
                ('usuario', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
