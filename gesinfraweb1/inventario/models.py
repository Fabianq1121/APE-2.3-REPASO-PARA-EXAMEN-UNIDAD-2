# inventario/models.py
from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    numero_inventario = models.CharField(
        max_length=50, 
        unique=True,
        verbose_name="Número de Inventario"
    )
    descripcion = models.CharField(
        max_length=200,
        verbose_name="Descripción del Equipo"
    )
    precio_adquisicion = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio de Adquisición"
    )
    usuario_responsable = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuario Responsable"
    )
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Registro"
    )
    estado = models.CharField(
        max_length=20,
        choices=[
            ('activo', 'Activo'),
            ('inactivo', 'Inactivo'),
            ('mantenimiento', 'En Mantenimiento'),
            ('baja', 'Dado de Baja')
        ],
        default='activo',
        verbose_name="Estado del Equipo"
    )
    
    def __str__(self):
        return f"{self.numero_inventario} - {self.descripcion}"
    
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['-fecha_registro']
