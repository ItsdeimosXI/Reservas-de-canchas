# backend/reservas/tasks.py
from celery import shared_task
from .models import Reservas
from datetime import datetime
import logging
logger = logging.getLogger('django')
@shared_task
def cambiar_estado_reservas():
    # Obtener la fecha y hora actual completa
    now = datetime.now()

    # Imprimir la fecha y hora actual para depuración
    print(f"Fecha y hora actual: {now}")
    
    # Obtener todas las reservas cuya fecha esté antes de la fecha actual y su hora esté entre horario_desde y horario_hasta
    reservas = Reservas.objects.filter(status='pendiente', horario_desde__lte=now, horario_hasta__gte=now)
    
    # Imprimir el número de reservas que se encontraron para depuración
    print(f"Se encontraron {reservas.count()} reservas para actualizar.")
    
    for reserva in reservas:
        # Imprimir los valores de las reservas para verificar los tiempos
        print(f"Reserva: {reserva.id}, Estado: {reserva.status}, Desde: {reserva.horario_desde}, Hasta: {reserva.horario_hasta}")
        
        reserva.status = 'completada'
        reserva.save()
    
    return "Estado de reservas actualizado a 'completada'."
    
