from __future__ import absolute_import, unicode_literals

# Asegura que Celery se cargue con Django
from .celery import app as celery_app

__all__ = ['celery_app']