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

class Area(models.Model):
	idarea=models.CharField(primary_key=True,default="-",max_length=16)
	nombre=models.CharField(default="-",max_length=20)

	def save(self,*args, **kwargs):
		super(Area,self).save(*args, **kwargs)
	def __str__(self):
		return self.nombre

class HelpMapper(models.Model):
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
	idarea = models.ForeignKey(Area, to_field='idarea', default="-")
	estado = models.IntegerField(default=1)

	def save(self,*args, **kwargs):
		super(HelpMapper,self).save(*args, **kwargs)

	def __str__(self):
		return self.id_HelpMapper

class Categoria(models.Model):
	nombreCategoria = models.CharField(max_length=30)
	unidad = models.CharField(max_length=20)

	def save(self,*args, **kwargs):
		super(Categoria,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombreCategoria

class Producto(models.Model):
	nombreProducto = models.CharField(max_length=30)
	cantidad = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
	idCategoria = models.ForeignKey(Categoria, to_field='id', default="-")

	def save(self,*args, **kwargs):
		super(Producto,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombreProducto


class CambioInventario(models.Model):
	tipo = models.IntegerField(default=1) #(-1) correccion  (0) envio  (1) ingreso
	cantidad = models.DecimalField(default=0.0,max_digits=6,decimal_places=2)
	idProducto = models.ForeignKey(Producto, to_field='id', default="-")
	fecha = models.DateField(default=datetime.date.today)

	def save(self,*args, **kwargs):
		super(CambioInventario,self).save(*args, **kwargs)

	def __str__(self):
		return self.id

class Administrador(models.Model):
	nombreUsuario = models.CharField(max_length=12, primary_key=True)
	contrasena = models.CharField( max_length=15)
	correo = models.EmailField(max_length=254)
	tipo = models.IntegerField(default=1) #(1) superAdmin, (0) adminCentro
	idCentro = models.ForeignKey(CentroDeAcopio, to_field='idCentro', default="-")
	estado = models.IntegerField(default=1)

	def save(self,*args, **kwargs):
		super(Administrador,self).save(*args, **kwargs)

	def __str__(self):
		return self.nombreUsuario

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
