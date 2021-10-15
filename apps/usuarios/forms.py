from django import forms
from .models import Medico, Paciente
from django.contrib.auth.models import User

class login_form(forms.Form):
    email = forms.EmailField(label="Correo", widget=forms.TextInput)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))

class register_form(forms.Form):
    email = forms.EmailField(label="Correo", widget=forms.TextInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(render_value=False))

    def clean_email(self):
        email = self.cleaned_data['email']
       
        try:
            c = User.objects.get(username = email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('El correo ingresado, ya se encuentra registrado')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
        else:
            raise forms.ValidationError('Las contraseñas no coinciden, intente de nuevo')


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
    numero = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Número de identificacion'}) )

class paciente_form(forms.ModelForm):
    model = Paciente
    field = '__all__'
    exclude = ['usuario']