from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from .forms import *


def inicio_view(request):
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
    object = Paciente.object.get(id = id_paciente)
    return render(request,'inicio/paciente_detalle.html', locals())

def generar_orden_view(request):
    return render(request,'inicio/generar_orden.html', locals())

def remitir_paciente_view(request):
    return render(request,'inicio/remitir_paciente.html', locals())
