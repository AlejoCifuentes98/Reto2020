from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    nombres      = models.CharField(max_length=250)
    apellidos    = models.CharField(max_length=250)
    telefono    = models.IntegerField()
    fecha_nacimineto = models.DateField()
    tipo = ('Medico, Paciente')
    rol        = models.charField(max_length=8, choices=tipo, default='Paciente')
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
    medico = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class OrdenMedica(models.Model):
    orden  = models.TextField()
    fecha  = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Orden del medico {}".format(self.medico)

class Especialista(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
    

class Remisiones(models.Model):
    especialista = models.ForeignKey(Especialista, on_delete=models.PROTECT)
    nota_medica  = models.TextField()

    def __str__(self):
        return "Remitido a {}".format(self.especialista)

    


