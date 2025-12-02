# inventario/forms.py (crear este archivo si no existe)
from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['numero_inventario', 'descripcion', 'precio_adquisicion', 'estado']
        
    def clean_numero_inventario(self):
        numero = self.cleaned_data.get('numero_inventario')
        # Validación personalizada si es necesario
        if not numero.startswith('INV-'):
            raise forms.ValidationError("El número debe comenzar con 'INV-'")
        return numero