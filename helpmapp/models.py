from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

TIPOS_SANGRES = (
	('A+', 'A+'),
	('A-', 'A-'),
	('B+', 'B+'),
	('B-', 'B-'),
	('AB+', 'AB+'),
	('AB-', 'AB-'),
	('O+', 'O+'),
	('O-', 'O-'),
	)


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


class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title
class Hability(models.Model):
	id=models.CharField(primary_key=True,default="-",max_length=16)
	nombre=models.CharField(default="-",max_length=20)

	def save(self,*args, **kwargs):
		super(Hability,self).save(*args, **kwargs)
	def __str__(self):
		return self.nombre

class AyudadorMapa(models.Model):
	idHelpMapper=models.CharField(default="-", primary_key=True,max_length=16)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	nombreUsuario = models.CharField(max_length=12)
	contrasena = models.CharField(max_length=15)
	sexo = models.CharField(max_length=10)	
	cedula = models.CharField( max_length=10)
	tipoSangre = models.CharField(max_length=5, default="O+", choices=TIPOS_SANGRES)
	telefono = models.CharField(max_length=10)		
	correo = models.EmailField(max_length=100)
	estado = models.IntegerField(default=1)
	

	def save(self,*args, **kwargs):
		super(AyudadorMapa,self).save(*args, **kwargs)

	def __str__(self):
		return self.idHelpMapper