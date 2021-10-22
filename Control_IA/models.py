from django.db import models

class Inventario_Alimentos(models.Model):

    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()

    
    def __str__(self):
        return self.nombre
    class Meta: 
        db_table = 'Inventario_Alimentos'
