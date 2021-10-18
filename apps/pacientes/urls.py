from django.urls import path
from .views import *

urlpatterns = [
    #Home para pacientes 
    path('inicio/',inicio_view, name='inicio'),
    
    path('mensaje/<int:id_atencion>/',mensajes_view, name='mensaje'),
    
    #sección de pacientes
    path('seleccionar_medico/',seleccionar_medico_view, name='seleccionar_medico'),
    path('cambiar_medico/<int:id_medico>/',cambiar_medico_view, name='cambiar_medico'),
    path('solicitar_atencion/', atencion_agregar_view, name='solicitar_atencion'),
    path('historial/',historial_view, name='historial'), #url para ver detalles de las citas del paciente

   
    
   
]