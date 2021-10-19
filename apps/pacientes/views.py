from django.shortcuts import render, redirect
from apps.usuarios.models import GrupoFamiliar
from .forms import *


def inicio_view(request):
    paciente= Paciente.objects.get(usuario=request.user.id)
    atenciones = AtencionMedica.objects.filter(grupo__paciente= paciente.id) 
    medico = GrupoFamiliar.objects.get(paciente = paciente.id)
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
    if Paciente.objects.filter(usuario = request.user.id).exists():
        nombre = Paciente.objects.get(usuario = request.user.id)
    else:
        nom = Medico.objects.get(usuario=request.user.id)
        nombre = "Doc. "+nom.nombre_completo()
    atencion = AtencionMedica.objects.get(id= id_atencion)
    mensaje = Mensaje.objects.filter(atencion=id_atencion)
    if request.method =='POST':
        form_m = mensaje_form(request.POST)
        if form_m.is_valid():
            m = form_m.save(commit=False)
            m.nombre=nombre
            m.atencion=atencion
            m.save()
    else:
        form_m = mensaje_form()
    return render(request,'inicio/mensajes.html', locals())
