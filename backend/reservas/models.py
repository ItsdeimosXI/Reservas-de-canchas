from django.db import models
from django.contrib.auth import get_user_model
from canchas.models import Canchas
# Create your models here.
class Reservas(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    dia = models.DateField()
    horario_desde = models.TimeField()
    horario_hasta = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendiente')
    usuario = models.ForeignKey(get_user_model(), db_column= 'user', verbose_name='Usuario', on_delete=models.CASCADE)
    cancha_reservada = models.ForeignKey(Canchas, on_delete = models.CASCADE)