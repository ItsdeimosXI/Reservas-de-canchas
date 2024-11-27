from django.shortcuts import render
from .serializer import CanchasSerializer, LugarSerializer
from .models import Canchas, Lugar
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.   
class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Canchas.objects.all()
    serializer_class = CanchasSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]