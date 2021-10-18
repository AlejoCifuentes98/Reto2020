from django import forms

from apps.usuarios.models import Especialidad
from .models import *


class atencion_form(forms.ModelForm):
    class Meta:
        model = AtencionMedica
        fields= '__all__'
        exclude = ['paciente']
        
class mensaje_form(forms.ModelForm):
    class Meta:
        model = Mensaje
        field = '__all__'
        exclude = ['nombre', 'atencion']

class orden_form(forms.ModelForm):
    class Meta:
        model = OrdenMedica
        field = '__all__'
        exclude = ['medico']

class especialidad_form(forms.ModelForm):
    class Meta:
        model = Especialidad
        field = '__all__'
        exclude = ['']

class remision_from(forms.ModelForm):
    class Meta:
        model = Remisiones
        field = '__all__'
        exclude = ['medico']




