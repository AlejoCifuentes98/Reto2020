from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from apps.usuarios.models import GrupoFamiliar
from .forms import *


def inicio_view(request):
    paciente= Paciente.objects.get(usuario=request.user.id)
    
    atenciones = AtencionMedica.objects.filter(paciente= paciente) 
    #paciente = Paciente.objects.get(usuario=usuario)
    medico = GrupoFamiliar.objects.get(paciente=paciente)
    return render(request,'inicio/inicio.html', locals())
    
def atencion_agregar_view(request):
    paciente = Paciente.objects.get(usuario=request.user.id)
    grupo    = GrupoFamiliar.objects.get(paciente= paciente)
    if request.method == 'POST':
        form_atencion = atencion_form(request.POST)
        if form_atencion.is_valid():
            a = form_atencion.save(commit=False)
            a.grupo = grupo
            a.save()
            return redirect('/inicio/')
    else:
        form_atencion = atencion_form() 
        return render(request, 'inicio/atencion_agregar.html', locals())    
    return render(request, 'inicio/atencion_agregar.html', locals())    

def seleccionar_medico_view(request):
    object = Medico.objects.filter(especialidad__nombre = "General")
    return render(request,'inicio/cambiar_medico.html', locals())

def cambiar_medico_view(request, id_medico):
    usuario = Paciente.objects.get(usuario = request.user.id)
    grupo = GrupoFamiliar.objects.get(paciente = usuario.id)
    medico = Medico.objects.get(id = id_medico)
    grupo.medico_cabecera = medico
    grupo.save()
    return redirect('/inicio/')

def historial_view(request):
    return render(request,'inicio/historial.html', locals())

def mensajes_view(request, id_atencion):
    if Paciente.objects.get(usuario = request.user.id):
        nombre = Paciente.objects.get(usuario = request.user.id)
    else:
        nombre = Medico.objects.get(usuario=request.user.id).exists()
    atencion = AtencionMedica.objects.get(id= id_atencion)
    mensaje = Mensaje.objects.filter(atencion=id_atencion)
    if request.method =='POST':
        form_m = mensaje_form(request.POST)
        if form_m.is_valid():
            m = form_m.save(commit=False)
            m.nombre=nombre.nombres
            m.atencion=atencion
            m.save()
    else:
        form_m = mensaje_form()
    return render(request,'inicio/mensajes.html', locals())
