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
                ('nombre_usuario', models.CharField(default=b'-', max_length=12, serialize=False, primary_key=True)),
                ('contrasena', models.CharField(default=b'-', max_length=15)),
                ('correo', models.EmailField(default=b'-', max_length=254)),
                ('tipo', models.IntegerField(default=1)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CambioInventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(default=1)),
                ('cantidad', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('fecha', models.DateField(auto_now=True)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_categoria', models.CharField(default=b'-', max_length=30)),
                ('unidad', models.CharField(default=b'-', max_length=20)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_upc', models.CharField(default=b'-', max_length=30)),
                ('direccion', models.CharField(default=b'-', max_length=100)),
                ('latitud', models.DecimalField(default=0.0, max_digits=15, decimal_places=10)),
                ('longitud', models.DecimalField(default=0.0, max_digits=15, decimal_places=10)),
                ('provincia', models.CharField(default=b'-', max_length=30)),
                ('canton', models.CharField(default=b'-', max_length=30)),
                ('estado', models.IntegerField(default=1)),
                ('almacenamiento_agua', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('almacenamiento_ropa', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('almacenamiento_comida', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('usuario_admin', models.ForeignKey(default=b'-', to='helpmapp.Administrador')),
            ],
        ),
        migrations.CreateModel(
            name='ExistenciaInventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('id_centro', models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio')),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('nombre', models.CharField(default=b'-', max_length=100)),
                ('apellido', models.CharField(default=b'-', max_length=100)),
                ('nombre_usuario', models.CharField(default=b'-', max_length=18, serialize=False, primary_key=True)),
                ('contrasena', models.CharField(default=b'-', max_length=15)),
                ('sexo', models.CharField(default=b'M', max_length=5, choices=[(b'M', b'M'), (b'F', b'F')])),
                ('cedula', models.CharField(default=b'-', max_length=10)),
                ('tipo_sangre', models.CharField(default=b'O+', max_length=5, choices=[(b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'AB+', b'AB+'), (b'AB-', b'AB-'), (b'O+', b'O+'), (b'O-', b'O-')])),
                ('telefono', models.CharField(default=b'-', max_length=10)),
                ('correo', models.EmailField(max_length=100)),
                ('habilidad', models.CharField(default=b'Primeros Auxilios', max_length=30, choices=[(b'Primeros Auxilios', b'Primeros Auxilios'), (b'Culinarias', b'Culinarias'), (b'Trabajo de Campo', b'Trabajo de Campo')])),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_producto', models.CharField(default=b'-', max_length=30)),
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
