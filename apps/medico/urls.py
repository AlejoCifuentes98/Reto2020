from django.urls import path
from .views import *

urlpatterns = [
     #sección de  medicos
    path('inicio/medico/',inicio_medico_view, name='inicio_medico'),
    path('paciente/detalle/<int:id_paciente>/',paciente_detalle_view, name='paciente_detalle'), 
    path('generar/orden/',generar_orden_view, name='generar_orden'),
    path('editar/orden/<int:id_orden>/',editar_orden_view, name='editar_orden'),
    path('eliminar/orden/<int:id_orden>/',eliminar_orden_view, name='eliminar_orden'),
    path('remitir/paciente/<int:id_paciente>',remitir_paciente_view, name='remitir_paciente'),
]
