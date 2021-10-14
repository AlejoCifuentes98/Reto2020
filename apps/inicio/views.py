from django.shortcuts import render

def inicio_view(request):
    return render(request,'inicio/inicio.html', locals())
def inicio_medico_view(request):
    return render(request,'inicio/inicio_medico.html', locals())

def login_view(request):
    return render(request,'inicio/login.html', locals())

def registro_view(request):
    return render(request,'inicio/registro.html', locals())
def logout_view(request):
    return render(request,'inicio/logout.html', locals())

def reportar_sintomas_view(request):
    return render(request,'inicio/reportar_sintomas.html', locals())

def cambiar_medico_view(request):
    return render(request,'inicio/cambiar_medico.html', locals())

def historial_view(request):
    return render(request,'inicio/historial.html', locals())

def paciente_detalle_view(request):
    return render(request,'inicio/paciente_detalle.html', locals())

def generar_orden_view(request):
    return render(request,'inicio/generar_orden.html', locals())

def remitir_paciente_view(request):
    return render(request,'inicio/remitir_paciente.html', locals())
