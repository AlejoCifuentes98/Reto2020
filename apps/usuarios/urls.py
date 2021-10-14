from django.urls import path
from .views import login_view, registro_view, registro_medico_view, logout_view

urlpatterns = [
      #Autencicación de usuarios
    path('login/',login_view, name='login'),
    path('registro/',registro_view, name='registro'),
    path('regis/tro_medico/',registro_medico_view, name='registro_medico'),
    path('logout/',logout_view, name='logout'),
]