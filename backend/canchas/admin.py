from django.contrib import admin
from .models import Canchas
# Register your models here.
class CanchasAdmin(admin.ModelAdmin):
    list_display=['nombre', 'numero_cancha', 'descripcion']

admin.site.register(Canchas, CanchasAdmin)
