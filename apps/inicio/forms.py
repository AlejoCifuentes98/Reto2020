from django import forms
from .models import *

class login_form(forms.Form):
    email = forms.EmailField(label="Correo", widget=forms.TextInput)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))

class register_form(forms.Form):
    email = forms.EmailField(label="Correo", widget=forms.TextInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(render_value=False))

class medico_form(forms.ModelForm):
    model = Medico
    field = '__all__'
    exclude = ['']

class paciente_form(forms.ModelForm):
    model = Paciente
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




