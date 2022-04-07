from django.db import models

# Create your models here.

class Departamentos(models.Model):

    reparticion=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Departamento de {self.reparticion}'

class Personal(models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.CharField(max_length=8)
    categoria=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} {self.apellido} | DNI: {self.dni} | Categoría: {self.categoria} | Email: {self.email}'

class Expedientes(models.Model):

    numero=models.CharField(max_length=10)
    estado=models.BooleanField()

    def __str__(self) -> str:
        return f'Expediente N° {self.numero} | Estado: {self.estado}'