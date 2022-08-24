from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo      = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    usuario     = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo + ' | ' + self.descripcion