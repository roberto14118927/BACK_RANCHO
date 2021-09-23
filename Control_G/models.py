from django.db import models
from django.db.models.deletion import CASCADE


class Raza(models.Model):
    raza = models.CharField(max_length=254)

    def __str__(self):
        return self.raza

    class Meta: 
        db_table = 'Raza'


class Ganado(models.Model):

    nombre = models.CharField(max_length=254)
    sexo = models.CharField(max_length=254)
    id_raza = models.ForeignKey(Raza, on_delete= models.CASCADE , related_name="id_raza")       #foreing Key 
    num_economico = models.CharField(max_length=254)
    num_registro = models.CharField(max_length=254)
    num_siniga = models.CharField(max_length=254)
    comentarios = models.CharField(max_length=254)

    dia_nacimiento = models.IntegerField()
    mes_nacimiento = models.IntegerField()
    anio_nacimiento = models.IntegerField()

    padre = models.CharField(max_length=254)
    madre = models.CharField(max_length=254)

    dia_entrada_hato = models.IntegerField()
    mes_entrada_hato = models.IntegerField()
    anio_entrada_hato = models.IntegerField()

    estado = models.CharField(max_length=254)
    condicion_estadia = models.CharField(max_length=254)


    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'Ganado'
