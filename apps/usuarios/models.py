from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Medico(models.Model):
    nombres        = models.CharField(max_length=50)
    apellidos      = models.CharField(max_length=50)
    telefono       = models.IntegerField()
    identificacion = models.IntegerField(unique=True)
    usuario          = models.ForeignKey(User, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre+''+self.apellidos
    

class Paciente(models.Model):
    nombres          = models.CharField(max_length=50)
    apellidos        = models.CharField(max_length=50)
    identificacion   = models.IntegerField(unique=True)
    telefono         = models.IntegerField()
    direcion         = models.CharField(max_length=200)
    usuario          = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_nacimineto = models.DateField()

    def __str__(self):
        return self.nombres+''+self.apellidos+''+str(self.identificacion)


class GrupoFamiliar(models.Model):
    titular = models.IntegerField()
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico_cabecera = models.ForeignKey(Medico, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.titular)
