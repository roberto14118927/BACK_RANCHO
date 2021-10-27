from django.contrib import admin
from apps.Ganado.Control_Peso.models import Peso_Ganando , Enfermedades_Ganado , Vacas_asociadas

# Register your models here.
admin.site.register(Peso_Ganando)
admin.site.register(Enfermedades_Ganado)
admin.site.register(Vacas_asociadas)