from django.db import models

# Create your models here.
class Producto(models.Model):
    Nombre = models.CharField(max_length=30)
    Precio = models.IntegerField()
    Descripción = models.CharField(max_length=100)
    Stock = models.IntegerField()
    Link = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=20)

class Usuario(models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Correo = models.CharField(max_length=30)
    Contraseña = models.CharField(max_length=20)
    Teléfono = models.IntegerField()

class Compra(models.Model):
    Id_Usuario = models.IntegerField()
    Precio_Total = models.IntegerField()

class Cantidad(models.Model):
    Id_Producto = models.IntegerField()
    Id_Compra = models.IntegerField()
    Cantidad = models.IntegerField()
    Precio_Cantidad = models.IntegerField()