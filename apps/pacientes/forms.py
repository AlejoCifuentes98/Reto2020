from django import forms
from apps.usuarios.models import Especialidad
from .models import *


class atencion_form(forms.ModelForm):
    class Meta:
        model = AtencionMedica
        fields= '__all__'
        exclude = ['grupo']
        
class mensaje_form(forms.ModelForm):
    class Meta:
        model = Mensaje
        field = '__all__'
        exclude = ['nombre', 'atencion']

class especialidad_form(forms.ModelForm):
    class Meta:
        model = Especialidad
        field = '__all__'
        exclude = ['']






