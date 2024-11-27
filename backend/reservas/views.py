from django.shortcuts import render
from .serializer import ReservasSerializer
from rest_framework import viewsets, permissions, generics
from .models import Reservas
# Create your views here.

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    
class GetReservasViewSet(generics.ListAPIView):
    serializer_class = ReservasSerializer
    def get_queryset(self):
        return Reservas.objects.filter(usuario=self.request.user)
