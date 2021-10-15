from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from apps.usuarios.models import GrupoFamiliar
from .forms import *


def inicio_view(request):
    paciente = Paciente.objects.get(id=request.user.id)
    atención = AtencionMedica.objects.filter(paciente=paciente)
    
    return render(request,'inicio/inicio.html', locals())

def inicio_medico_view(request):
    
    return render(request,'inicio/inicio_medico.html', locals())




def reportar_sintomas_view(request):
    return render(request,'inicio/reportar_sintomas.html', locals())

def cambiar_medico_view(request):
    return render(request,'inicio/cambiar_medico.html', locals())

def historial_view(request):
    return render(request,'inicio/historial.html', locals())

def paciente_detalle_view(request, id_paciente):
    paciente = Paciente.object.get(id = id_paciente)

    return render(request,'inicio/paciente_detalle.html', locals())

def generar_orden_view(request):
    return render(request,'inicio/generar_orden.html', locals())

def editar_orden_view(request, id_orden):
    return render(request,'inicio/editar_orden.html', locals())

def eliminar_orden_view(request,id_orden):
    return render(request,'inicio/eliminar_orden.html', locals())

def remitir_paciente_view(request, id_paciente):
    return render(request,'inicio/remitir_paciente.html', locals())
