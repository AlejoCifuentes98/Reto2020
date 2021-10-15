from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Medico(models.Model):
    nombres        = models.CharField(max_length=50)
    apellidos      = models.CharField(max_length=50)
    telefono       = models.IntegerField()
    identificacion = models.IntegerField(unique=True)
    usuario        = models.ForeignKey(User, on_delete=models.CASCADE)
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
    id_persona        = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    id_medico         = models.ForeignKey(Medico, on_delete=models.PROTECT)
    id_titular        = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
