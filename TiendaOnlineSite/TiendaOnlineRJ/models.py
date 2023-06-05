from django.db import models


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=30)

    objects = models.Manager()

    class Meta:
        db_table = 'usuario'


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=50, decimal_places=2)

    objects = models.Manager()

    class Meta:
        db_table = 'producto'


class Pedido(models.Model):
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        db_table = 'pedido'
