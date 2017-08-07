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
                ('id_Administrador', models.CharField(primary_key=True, max_length=16, serialize=False, default='-')),
                ('nombreUsuario', models.CharField(max_length=12)),
                ('contrasena', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo', models.IntegerField()),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CambioInventario',
            fields=[
                ('id_CambioInventario', models.CharField(primary_key=True, max_length=16, serialize=False, default='-')),
                ('tipo', models.IntegerField()),
                ('cantidad', models.DecimalField(default=0, decimal_places=2, max_digits=6)),
                ('fecha', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_Categoria', models.CharField(primary_key=True, max_length=16, serialize=False, default='-')),
                ('nombreCategoria', models.CharField(max_length=30)),
                ('unidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('id_Centro', models.CharField(primary_key=True, max_length=16, serialize=False, default='-')),
                ('nombreUPC', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('latitud', models.DecimalField(default=0, decimal_places=10, max_digits=15)),
                ('longitud', models.DecimalField(default=0, decimal_places=10, max_digits=15)),
                ('provincia', models.CharField(max_length=30)),
                ('canton', models.CharField(max_length=30)),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id_Habilidad', models.CharField(primary_key=True, max_length=16, serialize=False, default='-')),
                ('nombreHabilidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HabilidadHelpMapper',
            fields=[
                ('id_HabilidadHelpMapper', models.CharField(primary_key=True, max_length=16, serialize=False, default='-')),
                ('id_Habilidad', models.ForeignKey(default='-', to='helpmapp.Habilidad')),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('id_HelpMapper', models.CharField(primary_key=True, max_length=16, serialize=False, default='-')),
                ('nombreUsuario', models.CharField(max_length=12)),
                ('contrasena', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=100)),
                ('estado', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('tipoSangre', models.CharField(max_length=5)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_Producto', models.CharField(primary_key=True, max_length=16, serialize=False, default='-')),
                ('nombreProducto', models.CharField(max_length=30)),
                ('cantidad', models.DecimalField(default=0, decimal_places=2, max_digits=8)),
                ('id_Categoria', models.ForeignKey(default='-', to='helpmapp.Categoria')),
                ('id_Centro', models.ForeignKey(default='-', to='helpmapp.CentroDeAcopio')),
            ],
        ),
        migrations.AddField(
            model_name='habilidadhelpmapper',
            name='id_HelpMapper',
            field=models.ForeignKey(default='-', to='helpmapp.HelpMapper'),
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='id_producto',
            field=models.ForeignKey(default='-', to='helpmapp.Producto'),
        ),
        migrations.AddField(
            model_name='administrador',
            name='id_Centro',
            field=models.ForeignKey(default='-', to='helpmapp.CentroDeAcopio'),
        ),
    ]
