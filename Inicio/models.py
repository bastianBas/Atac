from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    rut = models.CharField(max_length=15)
    correo = models.EmailField(max_length=20)
    cargo = models.CharField(max_length=20)
    area = models.CharField(max_length=20)

   

