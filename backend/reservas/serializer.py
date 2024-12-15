from rest_framework import serializers
from .models import Reservas
class ReservasSerializer(serializers.ModelSerializer):
    nombre_cancha = serializers.ReadOnlyField(source='cancha_reservada.nombre')
    class Meta:
        model = Reservas
        fields = ['id', 'dia', 'horario_desde', 'horario_hasta','cancha_reservada', 'status', 'nombre_cancha']
