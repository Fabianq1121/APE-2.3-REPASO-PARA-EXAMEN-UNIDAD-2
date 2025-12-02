# inventario/admin.py
from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('numero_inventario', 'descripcion', 'precio_adquisicion', 
                   'estado', 'usuario_responsable', 'fecha_registro')
    list_filter = ('estado', 'fecha_registro', 'usuario_responsable')
    search_fields = ('numero_inventario', 'descripcion')
    ordering = ('-fecha_registro',)
    readonly_fields = ('fecha_registro',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_inventario', 'descripcion', 'precio_adquisicion', 'estado')
        }),
        ('Responsable', {
            'fields': ('usuario_responsable',)
        }),
        ('Registro', {
            'fields': ('fecha_registro',)
        }),
    )