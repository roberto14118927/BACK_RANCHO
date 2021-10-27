from django.contrib import admin
from apps.Users.Control_Medicos.models import Medico_Especialista , Empadre_medico

# Register your models here.
admin.site.register(Empadre_medico)
admin.site.register(Medico_Especialista)