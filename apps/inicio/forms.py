from django.forms import forms

class login_form(forms.Form):
    email = forms.EmailField(label="Correo", widget=forms.TextInput(attrs={}))
    password = forms.PasswordField(label="Contraseña", widget=forms.PasswordInput(render_value=False))

