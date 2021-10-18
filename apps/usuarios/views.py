from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import register_form, paciente_form, medico_form, login_form, buscar_form, register_grupo_form
from .models import Paciente, GrupoFamiliar, Medico
import random
# Create your views here.
def login_view(request):
    ema=""
    pas=""
    if request.method == 'POST':
        form_l = login_form(request.POST)
        if form_l.is_valid():
            ema = form_l.cleaned_data['email']
            pas = form_l.cleaned_data['password']
            usuario = authenticate(username=ema, password=pas)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                if Paciente.objects.filter(usuario = request.user.id).exists():
                    return redirect('/inicio/')
                else:
                    return redirect('/inicio/medico/')

            else:
                messages.error(request, "Error en el Email o Contraseña")
    else:
        form_l = login_form()
    return render(request,'usuario/login.html', locals())

def registro_view(request):
    numero = Medico.objects.filter(especialidad__nombre = 'General').count()
    n = random.randint(1,numero)
    medico = Medico.objects.get(id = n)
    if request.method == 'POST':
        form_u = register_form(request.POST)
        form_p = paciente_form(request.POST)
        if form_u.is_valid() and form_p.is_valid():
            ema = form_u.cleaned_data['email']
            pas = form_u.cleaned_data['password2']

            u = User.objects.create_user(username=ema, password=pas)
            p=form_p.save(commit=False)
            u.save()
            p.usuario=u
            p.save()
            GrupoFamiliar.objects.create(paciente=p, medico_cabecera=medico)
            return redirect('')
    else:
        form_u = register_form()
        form_p = paciente_form()
    return render(request,'usuario/registro.html', locals())

def registro_medico_view(request):
    if request.method == 'POST':
        form_u = register_form(request.POST)
        form_m = medico_form(request.POST)
        if form_u.is_valid() and form_m.is_valid():
            ema = form_u.cleaned_data['email']
            pas = form_u.cleaned_data['password2']

            u = User.objects.create_user(username=ema, password=pas)
            m=form_m.save(commit=False)
            u.save()
            m.usuario=u
            m.save()
            return redirect('/')
    else:
        form_u = register_form()
        form_m = medico_form()
    return render(request,'usuario/registro_medico.html', locals())

def logout_view(request):
    logout(request)
    return redirect('/')

def crear_famillia_view(request):
    usuario = Paciente.objects.get(usuario = request.user.id)
    grupo = GrupoFamiliar.objects.get(Paciente = usuario.id)
    grupo.titular = usuario
    return redirect('/inicio/')

def grupo_familiar_view(request):
    usuario = Paciente.objects.get(usuario = request.user.id)
    objects = GrupoFamiliar.objects.filter(titular = usuario.id)
   
    if request.method == 'GET':
        form_b = buscar_form(request.GET)
        if form_b.is_valid():
            num = form_b.cleaned_data['numero']
            buscar = Paciente.objects.get(identificacion__icontains  = num)
            if buscar:
                buscar
            else:
                messages.error(request, "Afiliado no encontrado")
    else:
        form_b = buscar_form()
    return render(request,'usuario/grupo_familiar.html', locals())

def crear_en_grupo_familiar_view(request):
    usuario = Paciente.objects.get(usuario = request.user.id)
    object  = GrupoFamiliar.objects.get(titular= usuario.id)
    if request.method == 'POST':
        form_a = register_grupo_form(request.POST)
        if form_a.is_valid():
            ide = form_a.cleaned_data['identificacion']
            ema = form_a.cleaned_data['email']
            u = User.objects.create_user(username=ema, password=ide)
            a = form_a.save(commit=False)
            u.save()
            a.usuario=u
            a.telefono=usuario.telefono
            a.direcion=usuario.direccion
            a.save()
            GrupoFamiliar.objects.create(paciente=a, titular=usuario.id, medico_cabecera=object.medico_cabecera)
            
            return redirect('/grupoFamiliar/')
    else:
        form_a= register_grupo_form()

    return render(request, 'grupo')
#Añadir a alguien a mi grupo familiar
#Funsion pensada para un boton
def add_grupo_familiar_view(request, id_afiliado):
    usuario = User.objects.get(id = request.user.id)
    object  = GrupoFamiliar.objects.get(titular= usuario)
   #afiliado = Paciente.objects.get(id=id_afiliado)
    GrupoFamiliar.objects.create(paciente=id_afiliado, titular=usuario.paciente.id, medico_cabecera=object.id)
    redirect('/grupo_familiar/')
    #return render(request,'usuario/grupo_familiar.html', locals())

            




