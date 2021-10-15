from django import forms

from apps.usuarios.models import Especialidad
from .models import *



class mensaje_form(forms.ModelForm):
    model = Mensaje
    field = '__all__'
    exclude = ['usuario']

class orden_form(forms.ModelForm):
    model = OrdenMedica
    field = '__all__'
    exclude = ['medico']

class especialidad_form(forms.ModelForm):
    model = Especialidad
    field = '__all__'
    exclude = ['']

class remision_from(forms.ModelForm):
    model = Remisiones
    field = '__all__'
    exclude = ['medico']




