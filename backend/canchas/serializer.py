from rest_framework import serializers
from .models import Canchas, Lugar

class CanchasSerializer(serializers.ModelSerializer):
    lugar = serializers.ReadOnlyField(source = 'lugar.nombre')
    class Meta:
        model = Canchas
        fields = ['id', 'nombre', 'numero_cancha', 'descripcion', 'lugar', 'tipo']

class LugarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Lugar
        fields = ['id', 'nombre']