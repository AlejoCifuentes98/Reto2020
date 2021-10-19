from django.shortcuts import render, redirect
from apps.usuarios.models import Paciente, Medico, GrupoFamiliar
from apps.pacientes.models import AtencionMedica
from .forms import  orden_form, remision_from
from .models import OrdenMedica, Remisiones
from datetime import date, datetime

#Vista de inicio de para el medico
def inicio_medico_view(request):
    medico = Medico.objects.get(usuario = request.user.id)
    atencion  = AtencionMedica.objects.filter(grupo__medico_cabecera= medico.id)
    paciente = GrupoFamiliar.objects.get(medico_cabecera = medico.id)
    return render(request,'medico/inicio_medico.html', locals())

#Vista de atender en la cual el medico atenderá al paciente
def atender_view(request, id_atencion):
    atencion = AtencionMedica.objects.get(id= id_atencion)
    orden    = OrdenMedica.objects.filter(atencion = atencion.id)
    remision = Remisiones.objects.filter(atencion = atencion)
    paciente = Paciente.objects.get(id = atencion.grupo.paciente.id)
    #Calcular la edad del paciente
    fecha = paciente.fecha_nacimineto
    edad =(( date.today() - fecha).days) / 365.2425
    edad = int(edad)
    return render(request, 'medico/atender.html', locals())


def generar_orden_view(request, id_atencion):
    atencion = AtencionMedica.objects.get(id= id_atencion)
    if request.method == 'POST':
        form_o = orden_form(request.POST)
        if form_o.is_valid():
            o = form_o.save(commit=False)
            o.atencion= atencion
            o.save()
            return redirect('/atender/{}/'.format(atencion.id))
    else:
        form_o = orden_form()
    return render(request,'medico/generar_orden.html', locals())

def editar_orden_view(request, id_orden):
    orden = OrdenMedica.object.get(id =id_orden)
    if request.method == 'POST':
        form_o = orden_form(request.POST, instance=orden)
        if form_o.is_valid():
            form_o.save()
            return redirect()
    else:
        form_o = orden_form(instance=orden)
    return render(request,'medico/editar_orden.html', locals())

def eliminar_orden_view(request,id_orden):
    orden = OrdenMedica.object.get(id = id_orden)
    orden.delete()
    return redirect ('')

def remitir_paciente_view(request, id_atencion):
    atencion = AtencionMedica.objects.get(id= id_atencion)
    if request.method == 'POST':
        form_r = remision_from(request.POST)
        if form_r.is_valid():
            r = form_r.save(commit=False)
            r.atencion = atencion
            r.save()
            redirect("/atender/{}/".format(atencion.id))
    else:
        form_r = remision_from()


    return render(request,'medico/remitir_paciente.html', locals())

def editar_remitir_view(request, id_remitir):
    remision = Remisiones.objects.get(id=id_remitir)
    if request.method == 'POST':
        form_r = remision_from(request.POST, instance=remision)
        if form_r.is_valid():
            form_r.save()
            redirect("hih")
    else:
        form_r = remision_from(instance=remision)
    return render(request,'medico/editar_remision.html', locals())

def eliminar_remitir_view(request, id_remitir):
    remision = Remisiones.objects.get(id=id_remitir)
    remision.delete()
    return redirect("hglg")
