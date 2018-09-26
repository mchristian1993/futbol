from django.contrib import admin
from .models import Equipos
@admin.register(Equipos)
class EquiposAdmin(admin.ModelAdmin):
    list_display = ['nombre_equipo', 'liga','tecnico']
# Register your models here.
