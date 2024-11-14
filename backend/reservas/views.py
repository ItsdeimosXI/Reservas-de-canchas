from django.shortcuts import render
from .serializer import ReservasSerializer
from rest_framework import viewsets, permissions
from .models import Reservas
# Create your views here.

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    def get_queryset(self):
        return Reservas.objects.filter(usuario=self.request.user)
