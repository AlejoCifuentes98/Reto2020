from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Medico(models.Model):
    nombres      = models.CharField(max_length=50)
    apellidos    = models.CharField(max_length=50)
    telefono    = models.IntegerField()
    identificacion = models.IntegerField(unique=True)
    correo = models.EmailField(unique=True, max_length=80)
    def __str__(self):
        return self.nombre+''+self.apellidos
               


class GrupoFamiliar(models.Model):
    nombre = models.CharField(max_length=250)
    medico_cabecera = models.ForeignKey(Medico, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
class Paciente(models.Model):
    nombres      = models.CharField(max_length=50)
    apellidos    = models.CharField(max_length=50)
    identificacion = models.IntegerField(unique=True)
    telefono    = models.IntegerField()
    correo = models.EmailField(unique=True, max_length=80)
    fecha_nacimineto = models.DateField()
    grupo_familiar= models.ForeignKey(GrupoFamiliar, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombres+''+self.apellidos+''+str(self.identificacion)
