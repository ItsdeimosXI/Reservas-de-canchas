from django.db import models
from django.contrib.auth import get_user_model
from canchas.models import Canchas
# Create your models here.
class Reservas(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    usuario = models.ForeignKey(get_user_model(), db_column= 'user', verbose_name='Usuario', on_delete=models.CASCADE)
    cancha_reservada = models.ForeignKey(Canchas, on_delete = models.CASCADE)