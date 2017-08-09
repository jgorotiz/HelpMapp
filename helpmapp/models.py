from django.db import models
import datetime
# Create your models here.

class CentroDeAcopio(models.Model):
	idCentro = models.CharField(default="-", primary_key=True,max_length=16)	
	nombreUPC = models.CharField(max_length=30)
	direccion = models.CharField(max_length=100)
	latitud = models.DecimalField(default=0.0,max_digits=15,decimal_places=10)
	longitud = models.DecimalField(default=0.0,max_digits=15,decimal_places=10)
	provincia = models.CharField(max_length=30)
	canton = models.CharField(max_length=30)
	estado = models.IntegerField(default=1)

	def save(self,*args, **kwargs):
		super(CentroDeAcopio,self).save(*args, **kwargs)

	def __str__(self):
		return self.idCentro

class HelpMapper(models.Model):
	idHelpMapper=models.CharField(default="-", primary_key=True,max_length=16)
	nombreUsuario = models.CharField(max_length=12)
	contrasena = models.CharField(max_length=15)
	correo = models.EmailField(max_length=100)
	estado = models.IntegerField(default=1)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	tipoSangre = models.CharField(max_length=5)
	cedula = models.CharField( max_length=10)
	telefono = models.CharField(max_length=10)
	sexo = models.CharField(max_length=10)

	def save(self,*args, **kwargs):
		super(HelpMapper,self).save(*args, **kwargs)

	def __str__(self):
		return self.idHelpMapper

class Habilidad(models.Model):
	idHabilidad = models.CharField(default="-",  primary_key=True,max_length=16)
	nombreHabilidad = models.CharField(max_length=100)

	def save(self,*args, **kwargs):
		super(Habilidad,self).save(*args, **kwargs)

	def __str__(self):
		return self.idHabilidad

