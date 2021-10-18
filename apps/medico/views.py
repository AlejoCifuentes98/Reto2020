from django.shortcuts import render, redirect
from apps.usuarios.models import Paciente, Medico, GrupoFamiliar
from .forms import  orden_form, remision_from
from .models import OrdenMedica, Remisiones
# Create your views here.

def inicio_medico_view(request):
    medico = Medico.objects.get(usuario = request.user.id)
    grupo  = GrupoFamiliar.objects.filter(medico_cabecera= medico.id)
    return render(request,'medico/inicio_medico.html', locals())

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
