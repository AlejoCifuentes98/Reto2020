from django import forms
from .models import Medico, Paciente

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