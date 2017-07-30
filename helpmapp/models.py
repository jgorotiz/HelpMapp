from django.db import models
import datetime
# Create your models here.


class HelpMapper(models.Model):
	id_HelpMapper = models.CharField( primary_key=True,max_length=16)
	nombre_usuario = models.CharField(max_length=12)
	contrasena = models.CharField(max_length=15)
	correo = models.EmailField(max_length=100)
	estado = models.IntegerField()
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	tipo_sangre = models.CharField(max_length=5)
	cedula = models.CharField( max_length=10)
	telefono = models.CharField(max_length=10)
	sexo = models.CharField(max_length=10)

	def save(self,*args, **kwargs):
		super(HelpMapper,self).save(*args, **kwargs)

	def __str__(self):
		return self.HelpMapper

class HabilidadHelpMapper(models.Model):
	id_HabilidadHelpMapper = models.CharField( primary_key=True,max_length=16)
	id_HelpMapper = models.CharField(max_length=16)
	id_Hablidad = models.CharField(max_length=16)

	def save(self,*args, **kwargs):
		super(HabilidadHelpMapper,self).save(*args, **kwargs)

	def __str__(self):
		return self.HabilidadHelpMapper

class Habilidad(models.Model):
	id_Habilidad = models.CharField( primary_key=True,max_length=16)
	nombre_habilidad = models.CharField(max_length=100)

	def save(self,*args, **kwargs):
		super(Habilidad,self).save(*args, **kwargs)

	def __str__(self):
		return self.Habilidad

class cambioInventario(models.Model):
	id_CambioInventario = models.CharField(primary_key=True,max_length=16)
	tipo = models.IntegerField() #(-1) correccion  (0) envio  (1) ingreso
	cantidad = models.DecimalField(default=0,max_digits=6,decimal_places=2)
	id_producto = models.CharField(max_length=16)
	fecha = models.DateField(default=datetime.date.today)

	def save(self,*args, **kwargs):
		super(cambioInventario,self).save(*args, **kwargs)

	def __str__(self):
		return self.cambioInventario

class Administrador(models.Model):
	idAdministrador = models.CharField(primary_key=True,max_length=16)
	nombreUsuario = models.CharField(max_length=12)
	contrasena = models.CharField( max_length=15)
	correo = models.EmailField(max_length=254)
	tipo = models.IntegerField()
	#revisar FK
	idCentro = models.CharField(max_length=16)
	estado = models.IntegerField()

	def save(self,*args, **kwargs):
		super(Administrador,self).save(*args, **kwargs)

	def __str__(self):
		return self.idAdministrador


class CentroDeAcopio(models.Model):
	idCentro = models.CharField(primary_key=True,max_length=16)	
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
		return self.idCentro

class Producto(models.Model):
	idProducto = models.CharField(primary_key=True,max_length=16)	
	nombreProducto = models.CharField(max_length=30)
	cantidad = models.DecimalField(default=0,max_digits=8,decimal_places=2)
	#revisar FK
	idCategoria = models.CharField(max_length=16)
	#revisar FK
	idCentro = models.CharField(max_length=16)

	def save(self,*args, **kwargs):
		super(Producto,self).save(*args, **kwargs)

	def __str__(self):
		return self.idProducto

class Categoria(models.Model):
	idCategoria = models.CharField(primary_key=True,max_length=16)	
	nombreCategoria = models.CharField(max_length=30)
	unidad = models.CharField(max_length=20)

	def save(self,*args, **kwargs):
		super(Categoria,self).save(*args, **kwargs)

	def __str__(self):
		return self.idCategoria

