from django.urls import path
from .views import login_view, registro_view, registro_medico_view, logout_view, grupo_familiar_view, crear_en_grupo_familiar_view, add_grupo_familiar_view,selecionar_view,crear_famillia_view

urlpatterns = [
      #Autencicación de usuarios
    path('login/',login_view, name='login'),
    path('registro/',registro_view, name='registro'),
    path('registro/seleccionar', selecionar_view, name='selecionar'),
    path('registro/medico/',registro_medico_view, name='registro_medico'),
    path('logout/',logout_view, name='logout'),
    path('seleccionar/<int:id_medico>/', crear_famillia_view, name='familia'),
    path('grupoFamiliar/', grupo_familiar_view, name='grupo_familiar'),
    path('grupoFamiliar/registrar/', crear_en_grupo_familiar_view, name='registra_familia'),
    path('grupoFamiliar/agregar/<int:id_afiliado>/', add_grupo_familiar_view, name='agregar_familia'),
]