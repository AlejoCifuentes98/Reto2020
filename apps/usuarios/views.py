from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import register_form, paciente_form, medico_form
from .models import Medico, Paciente
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form_l = login_form(request.POST)
        if form_l.is_valid():
            ema = form_l.cleaned_data['email']
            pas = form_l.cleaned_data['password']
            usuario = authenticate(email=ema, password=pas)
            if usuario is not None and usuario.is_active():
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.error(request, "Error en el Email o Contraseña")
    else:
        form_l = login_form()
    return render(request,'inicio/login.html', locals())

def registro_view(request):
    if request.method == 'POST':
        form_u = register_form(request.POST)
        form_p = paciente_form(request.POST)
        if form_u.is_valid() and form_p.is_valid():
            ema = form_u.cleaned_data['email']
            pas = form_u.cleaned_data['password']

            u = User.objects.create_user(username=ema, password=pas)
            p=form_p.save(commit=False)
            u.save()
            p.user=u
            p.save()

            return redirect('/inicio/')

    return render(request,'inicio/registro.html', locals())

def registro_medico_view(request):
    if request.method == 'POST':
        form_u = register_form(request.POST)
        form_m = medico_form(request.POST)
        if form_u.is_valid() and form_m.is_valid():
            ema = form_u.cleaned_data['email']
            pas = form_u.cleaned_data['password']

            u = User.objects.create_user(username=ema, password=pas)
            p=form_m.save(commit=False)
            u.save()
            p.user=u
            p.save()

            return redirect('/inicio/')
    return render(request,'inicio/registro.html', locals())


def logout_view(request):
    logout(request)
    return redirect('inicio')