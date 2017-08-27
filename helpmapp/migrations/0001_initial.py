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
                ('nombreUsuario', models.CharField(default='-', primary_key=True, max_length=12, serialize=False)),
                ('contrasena', models.CharField(default='-', max_length=15)),
                ('correo', models.EmailField(default='-', max_length=254)),
                ('tipo', models.IntegerField(default=1)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CambioInventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tipo', models.IntegerField(default=1)),
                ('cantidad', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(default='-', max_length=30)),
                ('unidad', models.CharField(default='-', max_length=20)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombreUPC', models.CharField(default='-', max_length=30)),
                ('direccion', models.CharField(default='-', max_length=100)),
                ('latitud', models.DecimalField(max_digits=15, default=0.0, decimal_places=10)),
                ('longitud', models.DecimalField(max_digits=15, default=0.0, decimal_places=10)),
                ('provincia', models.CharField(default='-', max_length=30)),
                ('canton', models.CharField(default='-', max_length=30)),
                ('estado', models.IntegerField(default=1)),
                ('almacenamientoAgua', models.DecimalField(max_digits=8, default=0.0, decimal_places=2)),
                ('almacenamientoRopa', models.DecimalField(max_digits=8, default=0.0, decimal_places=2)),
                ('almacenamientoComida', models.DecimalField(max_digits=8, default=0.0, decimal_places=2)),
                ('idAdmin', models.ForeignKey(default=1, to='helpmapp.Administrador')),
            ],
        ),
        migrations.CreateModel(
            name='ExistenciaInventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('idCentro', models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio')),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('nombre', models.CharField(default='-', max_length=100)),
                ('apellido', models.CharField(default='-', max_length=100)),
                ('nombre_usuario', models.CharField(default='-', primary_key=True, max_length=18, serialize=False)),
                ('contrasena', models.CharField(default='-', max_length=15)),
                ('sexo', models.CharField(default='M', max_length=5, choices=[('M', 'M'), ('F', 'F')])),
                ('cedula', models.CharField(default='-', max_length=10)),
                ('tipo_sangre', models.CharField(default='O+', max_length=5, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])),
                ('telefono', models.CharField(default='-', max_length=10)),
                ('correo', models.EmailField(max_length=100)),
                ('habilidad', models.CharField(default='Primeros Auxilios', max_length=30, choices=[('Primeros Auxilios', 'Primeros Auxilios'), ('Culinarias', 'Culinarias'), ('Trabajo de Campo', 'Trabajo de Campo')])),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(default='-', max_length=30)),
                ('estado', models.IntegerField(default=1)),
                ('idCategoria', models.ForeignKey(default=0, to='helpmapp.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='existenciainventario',
            name='idProducto',
            field=models.ForeignKey(default=0, to='helpmapp.Producto'),
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='idCentro',
            field=models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio'),
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='idProducto',
            field=models.ForeignKey(default=0, to='helpmapp.Producto'),
        ),
    ]
