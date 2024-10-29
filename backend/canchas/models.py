from django.db import models

# Create your models here.

class Canchas(models.Model):
    nombre = models.CharField(max_length=48)
    numero_cancha = models.IntegerField()
    descripcion = models.TextField(max_length=1086)

    def __str__(self):
        return (self.nombre)