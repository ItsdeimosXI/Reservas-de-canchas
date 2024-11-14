from django.db import models

# Create your models here.

class Canchas(models.Model):
    nombre = models.CharField(max_length=48)
    numero_cancha = models.IntegerField()
    descripcion = models.TextField(max_length=1086)
    lugar = models.ForeignKey('Lugar', on_delete=models.CASCADE)
    def __str__(self):
        return (self.nombre)
    
class Lugar(models.Model):
    nombre = models.CharField(max_length=48)
    def __str__(self):
        return (self.nombre)