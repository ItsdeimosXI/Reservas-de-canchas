from rest_framework import serializers
from .models import Reservas

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = ['id','dia', 'horario_desde', 'horario_hasta','cancha_reservada']
