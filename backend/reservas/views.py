from argparse import Action
from django.shortcuts import render
from .serializer import ReservasSerializer
from rest_framework import viewsets, permissions, generics
from .models import Reservas
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta
from canchas.models import Canchas
# Create your views here.

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    @action(detail=False, methods=['get'])
    def horas_ocupadas(self, request):
        fecha = '2024-11-29'
        cancha_id = '62'
        if not fecha:
            return Response({'error': 'Debe proporcionar una "fecha".'}, status=400)
        try:
            cancha = Canchas.objects.get(id=cancha_id)
        except cancha.DoesNotExist:
            return Response({'error': 'Debe proporcionar un "cancha_id".'}, status=400)
        fecha_inicio = datetime.strptime(fecha, "%Y-%m-%d")
        fecha_fin = fecha_inicio + timedelta(days=1)

        # Filtrar las reservas de la cancha seleccionada
        reservas = Reservas.objects.filter(cancha_reservada=cancha, horario_desde=fecha_inicio, horario_hasta=fecha_fin)
        print(reservas)
        

        horas_ocupadas = set()  # Usamos un conjunto para evitar duplicados
        for reserva in reservas:
            hora_actual = reserva.inicio
            while hora_actual < reserva.fin:
                horas_ocupadas.add(hora_actual.strftime("%H:%M"))
                hora_actual += timedelta(hours=1)

        return Response(sorted(list(horas_ocupadas)), status=200)
class GetReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Reservas.objects.filter(usuario=self.request.user)
