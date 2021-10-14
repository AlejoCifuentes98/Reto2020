from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from .forms import *


def inicio_view(request):
    return render(request,'inicio/inicio.html', locals())

def inicio_medico_view(request):
    
    return render(request,'inicio/inicio_medico.html', locals())

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

def reportar_sintomas_view(request):
    return render(request,'inicio/reportar_sintomas.html', locals())

def cambiar_medico_view(request):
    return render(request,'inicio/cambiar_medico.html', locals())

def historial_view(request):
    return render(request,'inicio/historial.html', locals())

def paciente_detalle_view(request, id_paciente):
    object = Paciente.object.get(id = id_paciente)
    return render(request,'inicio/paciente_detalle.html', locals())

def generar_orden_view(request):
    return render(request,'inicio/generar_orden.html', locals())

def remitir_paciente_view(request):
    return render(request,'inicio/remitir_paciente.html', locals())
