from argparse import Action
from django.shortcuts import render
from .serializer import ReservasSerializer
from rest_framework import viewsets, permissions
from .models import Reservas
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta, time
from canchas.models import Canchas

# Create your views here.

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    @action(detail=False, methods=['get'])
    def reservaciones(self, request):
        user = request.user


        if not request.user.is_authenticated:
            return Response({'error': 'Debe proporcionar debe estar autenticado.'}, status=400)
        reservaciones = Reservas.objects.filter(usuario=user)
        serializer = ReservasSerializer(reservaciones, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def horas_ocupadas(self, request):
        fecha = request.query_params.get('fecha')
        cancha_id = request.query_params.get('cancha_id')

        if not fecha:
            return Response({'error': 'Debe proporcionar una "fecha".'}, status=400)
        if not cancha_id:
            return Response({'error': 'Debe proporcionar un "cancha_id".'}, status=400)

        try:
            cancha = Canchas.objects.get(id=cancha_id)
        except Canchas.DoesNotExist:
            return Response({'error': 'La "cancha_id" proporcionada no existe.'}, status=404)

       
        fecha_inicio = datetime.strptime(fecha, "%Y-%m-%d").date()  
        hora_inicio = time(0, 0)  
        hora_fin = time(23, 59)  
        reservas = Reservas.objects.filter(
            cancha_reservada=cancha,
            dia=fecha_inicio,
            horario_desde__gte=hora_inicio,
            horario_hasta__lte=hora_fin
        )
  
        horas_ocupadas = set() 
        for reserva in reservas:
            hora_actual = datetime.combine(fecha_inicio, reserva.horario_desde)
            fin_reserva = datetime.combine(fecha_inicio, reserva.horario_hasta)

            while hora_actual < fin_reserva:
                horas_ocupadas.add(hora_actual.strftime("%H:%M"))
                hora_actual += timedelta(hours=1)

        return Response(sorted(list(horas_ocupadas)), status=200)
    
