# inventario/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Equipo
from .forms import EquipoForm

@login_required
def listar_equipos(request):
    """Vista para listar todos los equipos"""
    equipos = Equipo.objects.all()
    
    # Filtros opcionales
    estado = request.GET.get('estado')
    if estado:
        equipos = equipos.filter(estado=estado)
    
    context = {
        'equipos': equipos,
        'total_equipos': equipos.count(),
        'filtro_estado': estado
    }
    return render(request, 'inventario/listar_equipos.html', context)

@login_required
def crear_equipo(request):
    """Vista para crear un nuevo equipo"""
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.usuario_responsable = request.user
            equipo.save()
            messages.success(request, f'Equipo {equipo.numero_inventario} creado exitosamente.')
            return redirect('listar_equipos')
    else:
        form = EquipoForm()
    
    return render(request, 'inventario/crear_equipo.html', {'form': form})

@login_required
def detalle_equipo(request, id):
    """Vista para ver detalles de un equipo"""
    equipo = get_object_or_404(Equipo, id=id)
    return render(request, 'inventario/detalle_equipo.html', {'equipo': equipo})