from django.shortcuts import render

def inicio_view(request):
    return render(request,'inicio/inicio.html', locals())
def inicio_medico_view(request):
    return render(request,'inicio/inicio_medico.html', locals())
def inicio_view(request):
    return render(request,'inicio/inicio.html', locals())
