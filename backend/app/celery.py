# backend/app/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece el nombre del proyecto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# Crear una instancia de Celery
app = Celery('app')
app.conf.broker_url = 'redis://localhost:6379/0'

# Usamos la configuración de Celery de Django (en settings.py)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-descubrimiento de tareas en todas las aplicaciones Django
app.autodiscover_tasks()
