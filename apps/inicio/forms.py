from django import forms

from apps.usuarios.models import Especialidad
from .models import *

class reportar_sintomas_form(forms.Form):
    reporte = forms.Textarea(label="Reportar Sintomas", widget= forms.TextInput,attrs={"placeholder":"Describe claramente tus sintomas y signos vitales al medico"})

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




