from django.db import models
from django.db.models.deletion import CASCADE
from apps.Ganado.Control_Ganado.models import Ganado
from apps.Inventarios.Control_IMedicos.models import Inventario_Insumos

class Control_Vacunas(models.Model):
    
    id_medicamento = models.ForeignKey(Inventario_Insumos , on_delete=CASCADE)
    id_ganado = models.ForeignKey(Ganado , on_delete=CASCADE)
    fecha_vacunacion = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)