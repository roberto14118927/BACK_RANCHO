from django.contrib import admin
from apps.Ganado.Control_Ganado.models import Ganado , Raza

class RazaAdmin(admin.ModelAdmin):
    list_display = ('id' , 'raza')

# Register your models here.
admin.site.register(Ganado)
admin.site.register(Raza , RazaAdmin)