from django.db import models

class Inventario_Insumos(models.Model):

    nombre = models.CharField(max_length=255)
    tipo_insumo = models.CharField(max_length=254)
    cantidad = models.IntegerField()
    lote = models.CharField(max_length=254 , null=True)
    presentacion = models.FloatField(default=0)
    producto_total = models.FloatField()


    def __str__(self):
        return str(self.id)
        
    class Meta: 
        db_table = 'Inventario_Insumos'
