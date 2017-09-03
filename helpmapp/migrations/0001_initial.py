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
                ('nombre_usuario', models.CharField(max_length=12, serialize=False, primary_key=True, default='-')),
                ('contrasena', models.CharField(max_length=15, default='-')),
                ('correo', models.EmailField(max_length=254, default='-')),
                ('tipo', models.IntegerField(default=1)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CambioInventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('tipo', models.IntegerField(default=1)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=6, default=0.0)),
                ('fecha', models.DateField(auto_now=True)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre_categoria', models.CharField(max_length=30, default='-')),
                ('unidad', models.CharField(max_length=20, default='-')),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre_upc', models.CharField(max_length=30, default='-')),
                ('direccion', models.CharField(max_length=100, default='-')),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=15, default=0.0)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=15, default=0.0)),
                ('provincia', models.CharField(max_length=30, default='-')),
                ('canton', models.CharField(max_length=30, default='-')),
                ('estado', models.IntegerField(default=1)),
                ('almacenamiento_agua', models.DecimalField(decimal_places=2, max_digits=8, default=0.0)),
                ('almacenamiento_ropa', models.DecimalField(decimal_places=2, max_digits=8, default=0.0)),
                ('almacenamiento_comida', models.DecimalField(decimal_places=2, max_digits=8, default=0.0)),
                ('usuario_admin', models.ForeignKey(default='-', to='helpmapp.Administrador')),
            ],
        ),
        migrations.CreateModel(
            name='ExistenciaInventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=6, default=0.0)),
                ('id_centro', models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio')),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('nombre', models.CharField(max_length=100, default='-')),
                ('apellido', models.CharField(max_length=100, default='-')),
                ('nombre_usuario', models.CharField(max_length=18, serialize=False, primary_key=True, default='-')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre_producto', models.CharField(max_length=30, default='-')),
                ('estado', models.IntegerField(default=1)),
                ('id_categoria', models.ForeignKey(default=0, to='helpmapp.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='existenciainventario',
            name='id_producto',
            field=models.ForeignKey(default=0, to='helpmapp.Producto'),
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='id_centro',
            field=models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio'),
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='id_producto',
            field=models.ForeignKey(default=0, to='helpmapp.Producto'),
        ),
    ]
