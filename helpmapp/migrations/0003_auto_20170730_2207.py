# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0002_auto_20170726_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('idAdministrador', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('nombreUsuario', models.CharField(max_length=12)),
                ('contrasena', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo', models.IntegerField()),
                ('idCentro', models.CharField(max_length=16)),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cambioInventario',
            fields=[
                ('id_CambioInventario', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('tipo', models.IntegerField()),
                ('cantidad', models.DecimalField(max_digits=6, default=0, decimal_places=2)),
                ('id_producto', models.CharField(max_length=16)),
                ('fecha', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('nombreCategoria', models.CharField(max_length=30)),
                ('unidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('idCentro', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('nombreUPC', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('latitud', models.DecimalField(max_digits=15, default=0, decimal_places=10)),
                ('longitud', models.DecimalField(max_digits=15, default=0, decimal_places=10)),
                ('provincia', models.CharField(max_length=30)),
                ('canton', models.CharField(max_length=30)),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id_Habilidad', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('nombre_habilidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HabilidadHelpMapper',
            fields=[
                ('id_HabilidadHelpMapper', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('id_HelpMapper', models.CharField(max_length=16)),
                ('id_Hablidad', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('id_HelpMapper', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('nombre_usuario', models.CharField(max_length=12)),
                ('contrasena', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=100)),
                ('estado', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('tipo_sangre', models.CharField(max_length=5)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('nombreProducto', models.CharField(max_length=30)),
                ('cantidad', models.DecimalField(max_digits=8, default=0, decimal_places=2)),
                ('idCategoria', models.CharField(max_length=16)),
                ('idCentro', models.CharField(max_length=16)),
            ],
        ),
        migrations.DeleteModel(
            name='Component',
        ),
    ]
