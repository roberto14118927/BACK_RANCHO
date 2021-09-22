from django.db import models
from Control_E.models import Control_Empadre


class Inventario_termo(models.Model):

    num_canastilla = models.IntegerField()
    nombre_toro = models.CharField(max_length=254)
    raza = models.CharField(max_length=254)
    descripcion = models.CharField(max_length=254)
    cantidad = models.IntegerField()
    comentario = models.CharField(max_length=254)
    num_termo = models.IntegerField()

    def __str__(self):
        return self.num_termo

    class Meta: 
        db_table = 'Inventario_Termo'


class Empadre_Termo(models.Model):

    id_empadre = models.ForeignKey(Control_Empadre , on_delete= models.CASCADE)
    id_inv_termo = models.ForeignKey(Inventario_termo , on_delete= models.CASCADE)

    def __str__(self):
        return self.id_empadre

    class Meta: 
        db_table = 'Empadre_Termo'
