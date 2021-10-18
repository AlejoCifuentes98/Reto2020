from django.db import models
from apps.pacientes.models import AtencionMedica

# Create your models here.

class OrdenMedica(models.Model):
    fecha  = models.DateTimeField(auto_now_add=True)
    descripción = models.TextField(max_length=500)
    atencion = models.ForeignKey(AtencionMedica, on_delete=models.PROTECT)

    def __str__(self):
        return "Orden del medico {}".format(self.medico)


class Remisiones(models.Model):
    medico = models.CharField(max_length=50)
    descripción = models.TextField()
    atencion = models.ForeignKey(AtencionMedica, on_delete=models.CASCADE)
    def __str__(self):
        return "Remitido a {}".format(self.medico)