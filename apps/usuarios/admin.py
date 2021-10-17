from django.contrib import admin
from apps.usuarios.models import *

admin.site.register(Especialidad),
admin.site.register(Medico),
admin.site.register(GrupoFamiliar),
admin.site.register(Paciente)

