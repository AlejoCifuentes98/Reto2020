from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.models import Medico, Paciente

# Create your models here.


class Historia(models.Model):
    fecha_creacion= models.DateField(auto_now_add=True)
    observaciones = models.TextField(max_length=500)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


class AtencionMedica(models.Model):
    fecha_atencion= models.DateTimeField(auto_now_add=True)
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT) 

class Mensaje(models.Model):
    mensaje = models.TextField()
    hora    = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.mensaje


class OrdenMedica(models.Model):
    orden  = models.TextField()
    fecha  = models.DateTimeField(auto_add=True)
    descripción = models.TextField(max_length=500)
    atencion = models.ForeignKey(AtencionMedica, on_delete=models.PROTECT)

    def __str__(self):
        return "Orden del medico {}".format(self.medico)

class Especialidad(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
    

class Remisiones(models.Model):
    especialistad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)
    atencion   = models.ForeignKey(AtencionMedica, on_delete=models.PROTECT)

    def __str__(self):
        return "Remitido a {}".format(self.especialista)

    


