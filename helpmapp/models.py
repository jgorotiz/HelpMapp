from django.db import models

# Create your models here.

class Component(models.Model):
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.description

#IntegerField
class HelpMapper(models.Model):
	id_HelpMapper = models.CharField( primary_key=True,max_length=16)
    nombre_usuario = models.CharField(max_length=12)
    contrasenia = models.CharField(min_length=6,max_length=15)
    correo = models.EmailField(max_length=100)
    estado = models.IntegerField(max_digits=1)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_sangre = models.CharField(max_length=5)
    cedula = models.CharField(min_length=10,max_length=10)
    telefono = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10)

class HabilidadHelpMapper(models.Model):
	id_HabilidadHelpMapper = models.CharField( primary_key=True,max_length=16)
	id_HelpMapper = models.CharField(max_length=16)
	id_Hablidad = models.CharField(max_length=16)


class Habilidad(models.Model):
	id_Habilidad = models.CharField( primary_key=True,max_length=16)
	nombre_habilidad = models.CharField(max_length=100)

class cambioInventario(models.Model):
	id_CambioInventario = models.CharField(primary_key=True,max_length=16)
	tipo = models.IntegerField(max_digits=1) #(-1) correccion  (0) envio  (1) ingreso
	cantidad = models.DecimalField(default=0,max_digits=6,decimal_places=2)
	id_producto = models.CharField(max_length=16)
	fecha = models.DateField(default=datetime.date.today)

	




