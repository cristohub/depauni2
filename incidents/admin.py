# incidents/admin.py

from django.contrib import admin
from .models import Averia, AveriaTecnico

@admin.register(Averia)
class AveriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'departamento', 'tipo_averia', 'estado', 'fecha_reporte', 'coste')
    list_filter = ('tipo_averia', 'estado')
    readonly_fields =('fecha_reporte',)
    search_fields = ('descripcion', 'departamento__nombre')  
    ordering = ('-fecha_reporte',)


@admin.register(AveriaTecnico)
class AveriaTecnicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'averia', 'tecnico', 'fecha_resuelta')
    list_filter = ('tecnico', 'fecha_resuelta')
    search_fields = (
        'averia__descripcion',
        'tecnico__first_name',
        'tecnico__last_name1',
        'tecnico__last_name2'
    )
  
    ordering = ('-fecha_resuelta',)