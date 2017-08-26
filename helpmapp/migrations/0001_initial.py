# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('nombreUsuario', models.CharField(max_length=12, primary_key=True, default='-', serialize=False)),
                ('contrasena', models.CharField(max_length=15, default='-')),
                ('correo', models.EmailField(max_length=254, default='-')),
                ('tipo', models.IntegerField(default=1)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CambioInventario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tipo', models.IntegerField(default=1)),
                ('cantidad', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombreCategoria', models.CharField(max_length=30, default='-')),
                ('unidad', models.CharField(max_length=20, default='-')),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombreUPC', models.CharField(max_length=30, default='-')),
                ('direccion', models.CharField(max_length=100, default='-')),
                ('latitud', models.DecimalField(default=0.0, max_digits=15, decimal_places=10)),
                ('longitud', models.DecimalField(default=0.0, max_digits=15, decimal_places=10)),
                ('provincia', models.CharField(max_length=30, default='-')),
                ('canton', models.CharField(max_length=30, default='-')),
                ('estado', models.IntegerField(default=1)),
                ('almacenamientoAgua', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('almacenamientoRopa', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('almacenamientoComida', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('idAdmin', models.ForeignKey(default=1, to='helpmapp.Administrador')),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('nombre', models.CharField(max_length=100, default='-')),
                ('apellido', models.CharField(max_length=100, default='-')),
                ('nombre_usuario', models.CharField(max_length=18, primary_key=True, default='-', serialize=False)),
                ('contrasena', models.CharField(max_length=15, default='-')),
                ('sexo', models.CharField(max_length=5, default='M', choices=[('M', 'M'), ('F', 'F')])),
                ('cedula', models.CharField(max_length=10, default='-')),
                ('tipo_sangre', models.CharField(max_length=5, default='O+', choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])),
                ('telefono', models.CharField(max_length=10, default='-')),
                ('correo', models.EmailField(max_length=100)),
                ('habilidad', models.CharField(max_length=30, default='Primeros Auxilios', choices=[('Primeros Auxilios', 'Primeros Auxilios'), ('Culinarias', 'Culinarias'), ('Trabajo de Campo', 'Trabajo de Campo')])),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombreProducto', models.CharField(max_length=30, default='-')),
                ('cantidad', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('estado', models.IntegerField(default=1)),
                ('idCategoria', models.ForeignKey(default=0, to='helpmapp.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='idProducto',
            field=models.ForeignKey(default=0, to='helpmapp.Producto'),
        ),
    ]
