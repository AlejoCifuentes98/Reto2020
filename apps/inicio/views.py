from django.shortcuts import render, redirect
from django.contrib import messages
from apps.usuarios.models import GrupoFamiliar
from apps.inicio.forms import *


def inicio_view(request):

    paciente= Paciente.objects.get(usuario=request.user.id)    
    atenciones = AtencionMedica.objects.filter(paciente= paciente) 

    return render(request,'inicio/inicio.html', locals())


def atencion_agregar_view(request):
    paciente = Paciente.objects.get(usuario=request.user.id)
    if request.method == 'POST':
        form_atencion = atencion_form(request.POST)
        if form_atencion.is_valid():
            a = form_atencion.save(commit=False)
            a.paciente = paciente
            a.save()
            return redirect('/')
    else:
        form_atencion = atencion_form() 
        return render(request, 'inicio/atencion_agregar.html', locals())    
    return render(request, 'inicio/atencion_agregar.html', locals())    

def  atencion_editar_view(request, id_atencion):
    atencion = AtencionMedica.object.get(id =id_atencion)
    if request.method == 'POST':
        form_atencion = orden_form(request.POST, instance=atencion)
        if form_atencion.is_valid():
            form_atencion.save()
            return redirect()
    else:
        form_atencion= orden_form(instance=atencion)
    return render(request,'inicio/atencion_edirtar.html', locals())
   

def atencion_eliminar_view(request, id_atencion):
    atencion = OrdenMedica.object.get(id = id_atencion)
    atencion.delete()
    return redirect('/')


def inicio_medico_view(request):
    
    return render(request,'inicio/inicio_medico.html', locals())

def cambiar_medico_view(request):
    return render(request,'inicio/cambiar_medico.html', locals())

def historial_view(request, id_atencion):
    atencion = AtencionMedica.objects.get(id=id_atencion)
   
    return render(request,'inicio/historial.html', locals())

def paciente_detalle_view(request, id_paciente):
    paciente = Paciente.object.get(id = id_paciente)

    return render(request,'inicio/paciente_detalle.html', locals())

def generar_orden_view(request):
    if request.method == 'POST':
        form_o = orden_form(request.POST)
        if form_o.is_valid():
            form_o.save()
    else:
        form_o = orden_form()
    return render(request,'inicio/generar_orden.html', locals())

def editar_orden_view(request, id_orden):
    orden = OrdenMedica.object.get(id =id_orden)
    if request.method == 'POST':
        form_o = orden_form(request.POST, instance=orden)
        if form_o.is_valid():
            form_o.save()
            return redirect()
    else:
        form_o = orden_form(instance=orden)
    return render(request,'inicio/editar_orden.html', locals())

def eliminar_orden_view(request,id_orden):
    orden = OrdenMedica.object.get(id = id_orden)
    orden.delete()
    return render(request,'inicio/eliminar_orden.html', locals())

def remitir_paciente_view(request, id_atencion):
    if request.method == 'POST':
        form_r = remision_from(request.POST)
        if form_r.is_valid():
            r = form_r.save(commit=False)
            r.atencion = id_atencion
            r.save()
            redirect("fgu")
    else:
        form_r = remision_from()


    return render(request,'inicio/remitir_paciente.html', locals())

def editar_remitir_view(request, id_remitir):
    remision = Remisiones.objects.get(id=id_remitir)
    if request.method == 'POST':
        form_r = remision_from(request.POST, instance=remision)
        if form_r.is_valid():
            form_r.save()
            redirect("hih")
    else:
        form_r = remision_from(instance=remision)
    return render(request,'inicio/editar_remision.html', locals())

def eliminar_remitir_view(request, id_remitir):
    remision = Remisiones.objects.get(id=id_remitir)
    remision.delete()
    return redirect("hglg")

def mensajes_view(request, id_atencion):
    nombre = Paciente.objects.get(usuario = request.user.id).exists()
    nombre = Medico.objects.get(usuario=request.user.id).exists()
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

def eliminar_mensaje_view(request, id_mensaje):
    mensaje = Mensaje.objects.get(id= id_mensaje)
    mensaje.delete()
    return redirect("gfhc")