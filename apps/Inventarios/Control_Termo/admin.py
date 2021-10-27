from django.contrib import admin
from apps.Inventarios.Control_Termo.models import Inventario_termo , Empadre_Termo

# Register your models here.
admin.site.register(Inventario_termo)
admin.site.register(Empadre_Termo)