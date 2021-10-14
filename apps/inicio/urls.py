from django.urls import path
from .views import inicio_view, inicio_medico_view, login_view, registro_view, registro_medico_view, logout_view, reportar_sintomas_view, cambiar_medico_view, historial_view, paciente_detalle_view, generar_orden_view, generar_orden_medico_view, remitir_paciente_view

urlpatterns = [
    #Home para pacientes y medicos
    path('',inicio_view, name='inicio'),
    path('inicio/medico',inicio_medico_view, name='inicio_medico'),
    
    #Autencicación de usuarios
    path('login/',login_view, name='login'),
    path('registro/',registro_view, name='registro'),
    path('regis/tro_medico/',registro_medico_view, name='registro_medico'),
    path('logout/',logout_view, name='logout'),
    
    #sección de pacientes
    path('reportar_sintomas/',reportar_sintomas_view, name='reportar_sintomas'),
    path('cambiar_medico/',cambiar_medico_view, name='cambiar_medico'),
    path('historial/',historial_view, name='historial'), #url para ver detalles de las citas del paciente

    #sección de  medicos
    path('paciente/detalle/',paciente_detalle_view, name='paciente_detalle'),
    path('generar/orden/',generar_orden_view, name='generar_orden'),
    path('remitir/paciente/',remitir_paciente_view, name='remitir_paciente'),
    
   
]