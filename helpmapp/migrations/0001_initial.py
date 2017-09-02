# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('nombre_usuario', models.CharField(primary_key=True, serialize=False, max_length=12, default='-')),
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
                ('cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('fecha', models.DateField(auto_now=True)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre_categoria', models.CharField(max_length=30, default='-')),
                ('unidad', models.CharField(max_length=20, default='-')),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre_upc', models.CharField(max_length=30, default='-')),
                ('direccion', models.CharField(max_length=100, default='-')),
                ('latitud', models.DecimalField(decimal_places=10, default=0.0, max_digits=15)),
                ('longitud', models.DecimalField(decimal_places=10, default=0.0, max_digits=15)),
                ('provincia', models.CharField(max_length=30, default='-')),
                ('canton', models.CharField(max_length=30, default='-')),
                ('estado', models.IntegerField(default=1)),
                ('almacenamiento_agua', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('almacenamiento_ropa', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('almacenamiento_comida', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('usuario_admin', models.ForeignKey(to='helpmapp.Administrador', default='-')),
            ],
        ),
        migrations.CreateModel(
            name='ExistenciaInventario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('id_centro', models.ForeignKey(to='helpmapp.CentroDeAcopio', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('nombre', models.CharField(max_length=100, default='-')),
                ('apellido', models.CharField(max_length=100, default='-')),
                ('nombre_usuario', models.CharField(primary_key=True, serialize=False, max_length=18, default='-')),
                ('contrasena', models.CharField(max_length=15, default='-')),
                ('sexo', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=5, default='M')),
                ('cedula', models.CharField(max_length=10, default='-')),
                ('tipo_sangre', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5, default='O+')),
                ('telefono', models.CharField(max_length=10, default='-')),
                ('correo', models.EmailField(max_length=100)),
                ('habilidad', models.CharField(choices=[('Primeros Auxilios', 'Primeros Auxilios'), ('Culinarias', 'Culinarias'), ('Trabajo de Campo', 'Trabajo de Campo')], max_length=30, default='Primeros Auxilios')),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre_producto', models.CharField(max_length=30, default='-')),
                ('estado', models.IntegerField(default=1)),
                ('id_categoria', models.ForeignKey(to='helpmapp.Categoria', default=0)),
            ],
        ),
        migrations.AddField(
            model_name='existenciainventario',
            name='id_producto',
            field=models.ForeignKey(to='helpmapp.Producto', default=0),
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='id_centro',
            field=models.ForeignKey(to='helpmapp.CentroDeAcopio', default=0),
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='id_producto',
            field=models.ForeignKey(to='helpmapp.Producto', default=0),
        ),
    ]
