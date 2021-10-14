from django.db import models
from django.contrib.auth import User

# Create your models here.

class Usuario(models.Model):
    nombre      = models.CharField(max_length=250)
    apellido    = models.CharField(max_length=250)
    telefono    = models.IntegerField()
    fecha_nacimineto = models.DateField()
    user       = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Mensaje(models.Model):
    mensaje = models.TextField()
    hora    = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.mensaje

class GrupoFamiliar(models.Model):
    nombre = models.CharField(max_length=250)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class OrdenMedica(models.Model):
    orden  = models.TextField()
    fecha  = models.DateTimeField(auto_now_add=True)

class Especialista(models.Model):
    nombre = models.
    

class Remisiones(models.Model):


    


