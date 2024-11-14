from django.contrib import admin
from .models import Reservas
# Register your models here.

class ReservasAdmin(admin.ModelAdmin):
    list_display = ['user', 'cancha_reservada', 'dia', 'horario']

admin.site.register(Reservas, ReservasAdmin)