from django import forms
from .models import Remisiones, OrdenMedica

class remision_from(forms.ModelForm):
    class Meta:
        model = Remisiones
        field = '__all__'
        exclude = ['medico']


class orden_form(forms.ModelForm):
    class Meta:
        model = OrdenMedica
        field = '__all__'
        exclude = ['atencion']