from django import forms
from .models import *

class login_form(forms.Form):
    email = forms.EmailField(label="Correo", widget=forms.TextInput)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))

class usuario_form(forms.ModelForm):
    model = Usuario
    field = '__all__'
    exclude = ['']

class mensaje_form(forms.ModelForm):
    model = Mensaje
    field = '__all__'
    exclude = ['usuario']

class orden_form(forms.ModelForm):
    model = OrdenMedica
    field = '__all__'
    exclude = ['medico']

class especialista_form(forms.ModelForm):
    model = Especialista
    field = '__all__'
    exclude = ['']

class remision_from(forms.ModelForm):
    model = Remisiones
    field = '__all__'
    exclude = ['medico']




