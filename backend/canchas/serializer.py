from rest_framework import serializers
from .models import Canchas, Lugar

class CanchasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canchas
        fields = ['id', 'nombre', 'numero_cancha', 'descripcion', 'lugar']

class LugarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Lugar
        fields = ['id', 'nombre']