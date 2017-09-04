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
	nombre_categoria = models.CharField(default="-",max_length=30)
	unidad = models.CharField(default="-",max_length=20)
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo

	def save(self,*args, **kwargs):
		super(Categoria,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre_categoria

class Producto(models.Model):
	nombre_producto = models.CharField(default="-",max_length=30)
	id_categoria = models.ForeignKey(Categoria, to_field='id', default=0)
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo

	def save(self,*args, **kwargs):
		super(Producto,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre_producto
		
class Administrador(models.Model):
	nombre_usuario = models.CharField(default="-",max_length=12, primary_key=True)
	contrasena = models.CharField(default="-", max_length=15)
	correo = models.EmailField(default="-",max_length=254)
	tipo = models.IntegerField(default=1) #(0) superAdmin, (1) adminCentro
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo

	def save(self,*args, **kwargs):
		super(Administrador,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre_usuario

class CentroDeAcopio(models.Model):
	nombre_upc = models.CharField(default="-",max_length=30)
	direccion = models.CharField(default="-",max_length=100)
	latitud = models.DecimalField(default=0.0,max_digits=15,decimal_places=10)
	longitud = models.DecimalField(default=0.0,max_digits=15,decimal_places=10)
	provincia = models.CharField(default="-",max_length=30)
	canton = models.CharField(default="-",max_length=30)
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo
	almacenamiento_agua = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
	almacenamiento_ropa = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
	almacenamiento_comida = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
	usuario_admin = models.ForeignKey(Administrador, to_field='nombre_usuario', default='-')

	def save(self,*args, **kwargs):
		super(CentroDeAcopio,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre_upc

class ExistenciaInventario(models.Model):
	id_producto = models.ForeignKey(Producto, to_field='id', default=0)
	id_centro = models.ForeignKey(CentroDeAcopio, to_field='id', default=0)
	cantidad = models.DecimalField(default=0.0,max_digits=6,decimal_places=2)
	def save(self,*args, **kwargs):
		super(ExistenciaInventario,self).save(*args, **kwargs)

	def __str__(self):
		return str(self.id)+"centro: "+str(self.id_centro)

class CambioInventario(models.Model):
	tipo = models.IntegerField(default=1) #(-1) correccion  (0) envio  (1) ingreso
	cantidad = models.DecimalField(default=0.0,max_digits=6,decimal_places=2)
	id_producto = models.ForeignKey(Producto, to_field='id', default=0)
	id_centro = models.ForeignKey(CentroDeAcopio, to_field='id', default=0)
	fecha = models.DateField(auto_now=True)
	estado = models.IntegerField(default=1) #(1) activo   (0) inactivo

	def save(self,*args, **kwargs):
		super(CambioInventario,self).save(*args, **kwargs)

	def __str__(self):
		return self.id
