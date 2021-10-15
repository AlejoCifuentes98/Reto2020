from django import forms
from .models import Medico, Paciente

class login_form(forms.Form):
    email = forms.EmailField(label="Correo", widget=forms.TextInput)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))

class register_form(forms.Form):
    email = forms.EmailField(label="Correo", widget=forms.TextInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(render_value=False))

class register_grupo_form(forms.ModelForm):
    model = Paciente
    field = '__all__'
    exclude =['telefono, usuario, direccion']

class medico_form(forms.ModelForm):
    model = Medico
    field = '__all__'
    exclude = ['usuario']
    email = forms.EmailField(label="Correo", widget=forms.TextInput)

class buscar_form(forms.Form):
    numero = forms.IntegerField(widget=forms.NumberInput, placeholder='Número de identificacion')

class paciente_form(forms.ModelForm):
    model = Paciente
    field = '__all__'
    exclude = ['usuario']