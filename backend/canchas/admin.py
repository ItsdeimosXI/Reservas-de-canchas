from django.contrib import admin
from .models import Canchas, Lugar
# Register your models here.
class CanchasAdmin(admin.ModelAdmin):
    list_display=['nombre', 'numero_cancha', 'descripcion', 'lugar']

admin.site.register(Canchas, CanchasAdmin)

admin.site.register(Lugar)