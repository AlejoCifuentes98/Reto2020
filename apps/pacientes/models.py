from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.models import Medico, Paciente

# Create your models here.

class AtencionMedica(models.Model):
    fecha_atencion= models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(max_length=500)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    

class Mensaje(models.Model):
    mensaje = models.TextField()
    hora    = models.DateTimeField(auto_now_add=True)
    nombre  = models.CharField(max_length=160)
    atencion = models.ForeignKey(AtencionMedica, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.mensaje


    


