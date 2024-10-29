from django.contrib import admin
from .models import Reservas
# Register your models here.

class ReservasAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'cancha_reservada', 'dia_horario']

admin.site.register(Reservas, ReservasAdmin)