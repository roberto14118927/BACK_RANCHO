from django.db import models
from django.db.models.deletion import SET_NULL
from apps.Ganado.Control_Empadre.models import Control_Empadre
from apps.Ganado.Control_Ganado.models import Ganado


class Inventario_termo(models.Model):

    num_canastilla = models.IntegerField()
    id_ganado = models.ForeignKey(Ganado , on_delete= SET_NULL , null=True)
    descripcion = models.CharField(max_length=254, null=True , blank=True)
    cantidad = models.IntegerField()
    comentario = models.CharField(max_length=254 , null=True , blank=True)
    num_termo = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta: 
        db_table = 'Inventario_Termocriogenico'


class Empadre_Termo(models.Model):

    id_empadre = models.ForeignKey(Control_Empadre , on_delete= models.CASCADE)
    id_inv_termo = models.ForeignKey(Inventario_termo , on_delete= SET_NULL,null=True)

    def __str__(self):
        return str(self.id_empadre)

    class Meta: 
        db_table = 'Empadre_Termocriogenico'
