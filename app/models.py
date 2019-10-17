from django.db import models

# Create your models here.

class Productos(models.Model):
	_COLOR_TYPES = (
        (1, "Rojo"),
        (2, "Azul"),
        (3, "Amarillo"),
        (4, "Verde"),
        (5, "Blanco"),
        (6, "Negro"),
        (7, "Otro"),
    )

	_TIPO_TYPES = (
        (1, "Crop Top"),
        (2, "Gorro"),
        (3, "Bufanda"),
        (4, "Otro"),
    )

	nombre = models.CharField(max_length=45, blank=False)
	valor = models.IntegerField()
	color = models.IntegerField(choices=_COLOR_TYPES )
	tipo = models.IntegerField(choices=_TIPO_TYPES)
	stock = models.IntegerField()
	foto = models.ImageField(default=None)


class Novedades(models.Model):
	titulo = models.CharField(max_length=45, blank=False)
	cuerpo = models.CharField(max_length=100, blank=False)
	fecha = models.DateField(auto_now=True)


class Mensajes(models.Model):
	nombre = models.CharField(max_length=45, blank=False)
	correo = models.CharField(max_length=45, blank=False)
	descripcion = models.CharField(max_length=300, blank=False)
	foto = models.ImageField(default=None)
	fecha = models.DateField(auto_now=True)

class Carro(models.Model):
	contexto = models.ManyToManyField(Productos)

class Pedidos(models.Model):
	carrito = models.ForeignKey(
        'Carro', related_name='pedidos', on_delete=models.CASCADE)
	nombre = models.CharField(max_length=45, blank=False)
	correo = models.CharField(max_length=45, blank=False)
	ciudad = models.CharField(max_length=45, blank=False)
	precio = models.IntegerField()


class User(models.Model):
	nombre = models.CharField(max_length=45, blank=False)
	contraseña = models.CharField(max_length=45, blank=False)