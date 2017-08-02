from django.db import models
import datetime
# Create your models here.

class CentroDeAcopio(models.Model):
	id_Centro = models.CharField(default="-", primary_key=True,max_length=16)	
	nombreUPC = models.CharField(max_length=30)
	direccion = models.CharField(max_length=100)
	latitud = models.DecimalField(default=0,max_digits=15,decimal_places=10)
	longitud = models.DecimalField(default=0,max_digits=15,decimal_places=10)
	provincia = models.CharField(max_length=30)
	canton = models.CharField(max_length=30)
	estado = models.IntegerField()

	def save(self,*args, **kwargs):
		super(CentroDeAcopio,self).save(*args, **kwargs)

	def __str__(self):
		return self.id_Centro

class HelpMapper(models.Model):
	id_HelpMapper = models.CharField(default="-", primary_key=True,max_length=16)
	nombreUsuario = models.CharField(max_length=12)
	contrasena = models.CharField(max_length=15)
	correo = models.EmailField(max_length=100)
	estado = models.IntegerField()
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	tipoSangre = models.CharField(max_length=5)
	cedula = models.CharField( max_length=10)
	telefono = models.CharField(max_length=10)
	sexo = models.CharField(max_length=10)

	def save(self,*args, **kwargs):
		super(HelpMapper,self).save(*args, **kwargs)

	def __str__(self):
		return self.id_HelpMapper

class Habilidad(models.Model):
	id_Habilidad = models.CharField(default="-",  primary_key=True,max_length=16)
	nombreHabilidad = models.CharField(max_length=100)

	def save(self,*args, **kwargs):
		super(Habilidad,self).save(*args, **kwargs)

	def __str__(self):
		return self.id_Habilidad

class HabilidadHelpMapper(models.Model):
	id_HabilidadHelpMapper = models.CharField(default="-",  primary_key=True,max_length=16)
	id_HelpMapper = models.ForeignKey(HelpMapper, to_field='id_HelpMapper', default="-")
	id_Habilidad = models.ForeignKey(Habilidad, to_field='id_Habilidad', default="-")

	def save(self,*args, **kwargs):
		super(HabilidadHelpMapper,self).save(*args, **kwargs)

	def __str__(self):
		return self.id_HabilidadHelpMapper

class Categoria(models.Model):
	id_Categoria = models.CharField(default="-", primary_key=True,max_length=16)	
	nombreCategoria = models.CharField(max_length=30)
	unidad = models.CharField(max_length=20)

	def save(self,*args, **kwargs):
		super(Categoria,self).save(*args, **kwargs)

	def __str__(self):
		return self.id_Categoria

class Producto(models.Model):
	id_Producto = models.CharField(default="-", primary_key=True,max_length=16)	
	nombreProducto = models.CharField(max_length=30)
	cantidad = models.DecimalField(default=0,max_digits=8,decimal_places=2)
	id_Categoria = models.ForeignKey(Categoria, to_field='id_Categoria', default="-")
	id_Centro = models.ForeignKey(CentroDeAcopio, to_field='id_Centro', default="-")

	def save(self,*args, **kwargs):
		super(Producto,self).save(*args, **kwargs)

	def __str__(self):
		return self.id_Producto


class CambioInventario(models.Model):
	id_CambioInventario = models.CharField(default="-", primary_key=True,max_length=16)
	tipo = models.IntegerField() #(-1) correccion  (0) envio  (1) ingreso
	cantidad = models.DecimalField(default=0,max_digits=6,decimal_places=2)
	id_producto = models.ForeignKey(Producto, to_field='id_Producto', default="-")
	fecha = models.DateField(default=datetime.date.today)

	def save(self,*args, **kwargs):
		super(CambioInventario,self).save(*args, **kwargs)

	def __str__(self):
		return self.id_CambioInventario

class Administrador(models.Model):
	id_Administrador = models.CharField(default="-", primary_key=True,max_length=16)
	nombreUsuario = models.CharField(max_length=12)
	contrasena = models.CharField( max_length=15)
	correo = models.EmailField(max_length=254)
	tipo = models.IntegerField()
	id_Centro = models.ForeignKey(CentroDeAcopio, to_field='id_Centro', default="-")
	estado = models.IntegerField()

	def save(self,*args, **kwargs):
		super(Administrador,self).save(*args, **kwargs)

	def __str__(self):
		return self.id_Administrador
