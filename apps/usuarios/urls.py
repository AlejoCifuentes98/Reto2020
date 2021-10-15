from django.urls import path
from .views import login_view, registro_view, registro_medico_view, logout_view, grupo_familiar_view

urlpatterns = [
      #Autencicación de usuarios
    path('login/',login_view, name='login'),
    path('registro/',registro_view, name='registro'),
    path('registro/medico/',registro_medico_view, name='registro_medico'),
    path('logout/',logout_view, name='logout'),
    path('grupoFamiliar/', grupo_familiar_view, name='grupo_familiar'),
]