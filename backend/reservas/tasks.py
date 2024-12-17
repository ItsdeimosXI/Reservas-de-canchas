from celery import shared_task
from .models import Reservas
from django.utils.timezone import now
import logging
logger = logging.getLogger('django')
@shared_task
def cambiar_estado_reservas():
    reservas_actualizadas = Reservas.objects.filter(
        status='pendiente', 
        horario_hasta__lt=now(),
    ).update(status='completada')

    return f"{reservas_actualizadas} reservas actualizadas."
    
