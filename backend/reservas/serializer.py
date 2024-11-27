from rest_framework import serializers
from .models import Reservas

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = ['id','dia', 'horario', 'cancha_reservada', 'usuario']
