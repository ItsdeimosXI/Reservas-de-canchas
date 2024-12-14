from django.apps import AppConfig


class ReservasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservas'
    def ready(self):
        import reservas.tasks  # Asegúrate de que Celery cargue las tareas al iniciar la aplicación
# backend/reservas/apps.py


