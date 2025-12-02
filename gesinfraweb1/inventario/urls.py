# inventario/urls.py (crear este archivo si no existe)
from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.listar_equipos, name='listar_equipos'),
    path('nuevo/', views.crear_equipo, name='crear_equipo'),
    path('<int:id>/', views.detalle_equipo, name='detalle_equipo'),
]
