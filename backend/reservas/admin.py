from django.contrib import admin
from .models import Reservas
# Register your models here.

class ReservasAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'cancha_reservada', 'dia', 'horario_desde' , 'horario_hasta']

admin.site.register(Reservas, ReservasAdmin)