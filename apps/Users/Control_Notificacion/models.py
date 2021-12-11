from django.db import models
from django.db.models.deletion import CASCADE
from apps.Users.Control_Usuario.models import User

class Control_Notificacion(models.Model):

    asunto = models.CharField(max_length=254)
    mensaje = models.CharField(max_length=254)
    id_user_emisor = models.ForeignKey(User , related_name='user_emisor' , on_delete=CASCADE  )
    id_user_receptor = models.ForeignKey(User ,  related_name='user_receptor' ,on_delete=CASCADE)
    estado = models.CharField(max_length=254)
    fecha = models.CharField(max_length=254)
    hora = models.CharField(max_length=254)

    def __str__(self):
        return str(self.id)