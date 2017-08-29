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

HABILIDADES = (
	('Primeros Auxilios', 'Primeros Auxilios'),
	('Culinarias', 'Culinarias'),
	('Trabajo de Campo', 'Trabajo de Campo'),
	)

SEXOS = (
	('M', 'M'),
	('F', 'F'),
	)



class HelpMapper(models.Model):
	nombre = models.CharField(default="-",max_length=100)
	apellido = models.CharField(default="-",max_length=100)
	nombre_usuario = models.CharField(default="-",max_length=18, primary_key=True)
	contrasena = models.CharField(default="-",max_length=15)
	sexo = models.CharField(default='M',max_length=5, choices=SEXOS)	
	cedula = models.CharField(default="-", max_length=10)
	tipo_sangre = models.CharField(max_length=5, default="O+", choices=TIPOS_SANGRES)
	telefono = models.CharField(default="-",max_length=10)		
	correo = models.EmailField(max_length=100)
	habilidad = models.CharField(max_length=30, default="Primeros Auxilios", choices=HABILIDADES)
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo

	def save(self,*args, **kwargs):
		super(HelpMapper,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre_usuario

class Categoria(models.Model):
	nombreCategoria = models.CharField(default="-",max_length=30)
	unidad = models.CharField(default="-",max_length=20)
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo

	def save(self,*args, **kwargs):
		super(Categoria,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombreCategoria

class Producto(models.Model):
	nombreProducto = models.CharField(default="-",max_length=30)
	idCategoria = models.ForeignKey(Categoria, to_field='id', default=0)
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo

	def save(self,*args, **kwargs):
		super(Producto,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombreProducto
		
class Administrador(models.Model):
	nombreUsuario = models.CharField(default="-",max_length=12, primary_key=True)
	contrasena = models.CharField(default="-", max_length=15)
	correo = models.EmailField(default="-",max_length=254)
	tipo = models.IntegerField(default=1) #(1) superAdmin, (0) adminCentro
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo

	def save(self,*args, **kwargs):
		super(Administrador,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombreUsuario

class CentroDeAcopio(models.Model):
	nombreUPC = models.CharField(default="-",max_length=30)
	direccion = models.CharField(default="-",max_length=100)
	latitud = models.DecimalField(default=0.0,max_digits=15,decimal_places=10)
	longitud = models.DecimalField(default=0.0,max_digits=15,decimal_places=10)
	provincia = models.CharField(default="-",max_length=30)
	canton = models.CharField(default="-",max_length=30)
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo
	almacenamientoAgua = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
	almacenamientoRopa = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
	almacenamientoComida = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
	idAdmin = models.ForeignKey(Administrador, to_field='nombreUsuario', default=1)

	def save(self,*args, **kwargs):
		super(CentroDeAcopio,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombreUPC

class ExistenciaInventario(models.Model):
	idProducto = models.ForeignKey(Producto, to_field='id', default=0)
	idCentro = models.ForeignKey(CentroDeAcopio, to_field='id', default=0)
	cantidad = models.DecimalField(default=0.0,max_digits=6,decimal_places=2)
	def save(self,*args, **kwargs):
		super(ExistenciaInventario,self).save(*args, **kwargs)

	def __str__(self):
		return self.id

class CambioInventario(models.Model):
	tipo = models.IntegerField(default=1) #(-1) correccion  (0) envio  (1) ingreso
	cantidad = models.DecimalField(default=0.0,max_digits=6,decimal_places=2)
	idProducto = models.ForeignKey(Producto, to_field='id', default=0)
	idCentro = models.ForeignKey(CentroDeAcopio, to_field='id', default=0)
	fecha = models.DateField(auto_now=True)
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo

	def save(self,*args, **kwargs):
		super(CambioInventario,self).save(*args, **kwargs)

	def __str__(self):
		return self.id




