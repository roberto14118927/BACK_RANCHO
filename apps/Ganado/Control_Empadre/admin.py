from django.contrib import admin
from apps.Ganado.Control_Empadre.models import Control_Empadre , Tacto
# Register your models here.

class GanadoAdmin(admin.ModelAdmin):
    list_display = ('id' , 'nombre')

admin.site.register(Control_Empadre)
admin.site.register(Tacto)