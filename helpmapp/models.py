from django.db import models

# Create your models here.

class Component(models.Model):
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.description


class Administrador(models.Model):
	idAdministrador = models.CharField(primary_key=True,max_length=16)
	nombreUsuario = models.CharField(max_length=12)
	contrasena = models.CharField(min_length=6, max_length=15)
	correo = models.EmailField(max_length=254)
	tipo = models.IntegerField(max_digits=1)
	#revisar FK
	idCentro = models.CharField(max_length=16)
	estado = models.IntegerField(max_digits=1)

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
	estado = models.IntegerField(max_digits=1)

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

