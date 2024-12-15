# backend/reservas/tasks.py
from celery import shared_task
from .models import Reservas
from django.utils.timezone import now
import logging
logger = logging.getLogger('django')
@shared_task
def cambiar_estado_reservas():
    # Obtener la fecha y hora actual completa
    tiempo_actual = now().time().strftime('%H:%M')
    dia_actual = now().date()
    
    # Obtener todas las reservas cuya fecha esté antes de la fecha actual y su hora esté entre horario_desde y horario_hasta
    reservas = Reservas.objects.filter(status='pendiente', horario_desde__lte=tiempo_actual, horario_hasta__gte=tiempo_actual, dia__lte=dia_actual)
    
    # Imprimir el número de reservas que se encontraron para depuración
    print(f"Se encontraron {reservas.count()} reservas para actualizar.")
    
    for reserva in reservas:
        # Imprimir los valores de las reservas para verificar los tiempos
        print(f"Reserva: {reserva.id}, Estado: {reserva.status}, Desde: {reserva.horario_desde}, Hasta: {reserva.horario_hasta}")
        
        reserva.status = 'completada'
        reserva.save()
    
    return "Estado de reservas actualizado a 'completada'."
    
