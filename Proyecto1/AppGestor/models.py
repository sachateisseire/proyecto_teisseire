from django.db import models

# Create your models here.

class Departamentos(models.Model):

    reparticion=models.CharField(max_length=50)

class Personal(models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.CharField(max_length=8)
    categoria=models.CharField(max_length=20)
    email=models.EmailField()

class Expedientes(models.Model):

    numero=models.CharField(max_length=10)
    estado=models.BooleanField()