from django.db import models

# Create your models here.

class Ingrediente(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

	def __str__(self):
		return '%s' % (self.nombre)

class Receta(models.Model):
	nombre = models.CharField(max_length=30)
	ingredientes = models.ManyToManyField(Ingrediente)
	instrucciones = models.TextField()
	fecha = models.DateTimeField()

	def __str__(self):
		return '%s' % (self.nombre)

