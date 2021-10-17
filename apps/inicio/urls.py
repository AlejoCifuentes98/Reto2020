from django.urls import path
from .views import inicio_view, inicio_medico_view, cambiar_medico_view, historial_view, mensajes_view, paciente_detalle_view, generar_orden_view, editar_orden_view,eliminar_orden_view, remitir_paciente_view

urlpatterns = [
    #Home para pacientes y medicos
    path('inicio/',inicio_view, name='inicio'),
    path('inicio/medico/',inicio_medico_view, name='inicio_medico'),
    
    path('mensaje/<int:id_atencion>/',mensajes_view, name='mensaje'),
    
    #sección de pacientes
    path('cambiar_medico/',cambiar_medico_view, name='cambiar_medico'),
    path('historial/',historial_view, name='historial'), #url para ver detalles de las citas del paciente

    #sección de  medicos
    path('paciente/detalle/<int:id_paciente>/',paciente_detalle_view, name='paciente_detalle'), 
    path('generar/orden/',generar_orden_view, name='generar_orden'),
    path('editar/orden/<int:id_orden>/',editar_orden_view, name='editar_orden'),
    path('eliminar/orden/<int:id_orden>/',eliminar_orden_view, name='eliminar_orden'),
    path('remitir/paciente/<int:id_paciente>',remitir_paciente_view, name='remitir_paciente'),
    
   
]