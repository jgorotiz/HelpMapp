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
<<<<<<< HEAD
                ('nombre_usuario', models.CharField(default=b'-', max_length=12, serialize=False, primary_key=True)),
                ('contrasena', models.CharField(default=b'-', max_length=15)),
                ('correo', models.EmailField(default=b'-', max_length=254)),
=======
<<<<<<< HEAD
                ('nombre_usuario', models.CharField(primary_key=True, max_length=12, serialize=False, default='-')),
=======
                ('nombre_usuario', models.CharField(primary_key=True, serialize=False, max_length=12, default='-')),
>>>>>>> 257318312f812d903fc2bead76200858d775501c
                ('contrasena', models.CharField(max_length=15, default='-')),
                ('correo', models.EmailField(max_length=254, default='-')),
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
                ('tipo', models.IntegerField(default=1)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CambioInventario',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(default=1)),
                ('cantidad', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
=======
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tipo', models.IntegerField(default=1)),
                ('cantidad', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
=======
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tipo', models.IntegerField(default=1)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
>>>>>>> 257318312f812d903fc2bead76200858d775501c
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
                ('fecha', models.DateField(auto_now=True)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_categoria', models.CharField(default=b'-', max_length=30)),
                ('unidad', models.CharField(default=b'-', max_length=20)),
=======
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
=======
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
>>>>>>> 257318312f812d903fc2bead76200858d775501c
                ('nombre_categoria', models.CharField(max_length=30, default='-')),
                ('unidad', models.CharField(max_length=20, default='-')),
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
<<<<<<< HEAD
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
                ('usuarioAdmin', models.ForeignKey(to='helpmapp.Administrador', default=b'-', to_field=b'nombreUsuario')),
=======
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre_upc', models.CharField(max_length=30, default='-')),
                ('direccion', models.CharField(max_length=100, default='-')),
                ('latitud', models.DecimalField(max_digits=15, decimal_places=10, default=0.0)),
                ('longitud', models.DecimalField(max_digits=15, decimal_places=10, default=0.0)),
                ('provincia', models.CharField(max_length=30, default='-')),
                ('canton', models.CharField(max_length=30, default='-')),
                ('estado', models.IntegerField(default=1)),
                ('almacenamiento_agua', models.DecimalField(max_digits=8, decimal_places=2, default=0.0)),
                ('almacenamiento_ropa', models.DecimalField(max_digits=8, decimal_places=2, default=0.0)),
                ('almacenamiento_comida', models.DecimalField(max_digits=8, decimal_places=2, default=0.0)),
                ('usuarioAdmin', models.ForeignKey(to_field='nombreUsuario', to='helpmapp.Administrador', default='-')),
=======
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
>>>>>>> 257318312f812d903fc2bead76200858d775501c
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
            ],
        ),
        migrations.CreateModel(
            name='ExistenciaInventario',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('id_centro', models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio')),
=======
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
=======
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
>>>>>>> 257318312f812d903fc2bead76200858d775501c
                ('id_centro', models.ForeignKey(to='helpmapp.CentroDeAcopio', default=0)),
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
<<<<<<< HEAD
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
=======
                ('nombre', models.CharField(max_length=100, default='-')),
                ('apellido', models.CharField(max_length=100, default='-')),
<<<<<<< HEAD
                ('nombre_usuario', models.CharField(primary_key=True, max_length=18, serialize=False, default='-')),
=======
                ('nombre_usuario', models.CharField(primary_key=True, serialize=False, max_length=18, default='-')),
>>>>>>> 257318312f812d903fc2bead76200858d775501c
                ('contrasena', models.CharField(max_length=15, default='-')),
                ('sexo', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=5, default='M')),
                ('cedula', models.CharField(max_length=10, default='-')),
                ('tipo_sangre', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5, default='O+')),
                ('telefono', models.CharField(max_length=10, default='-')),
                ('correo', models.EmailField(max_length=100)),
                ('habilidad', models.CharField(choices=[('Primeros Auxilios', 'Primeros Auxilios'), ('Culinarias', 'Culinarias'), ('Trabajo de Campo', 'Trabajo de Campo')], max_length=30, default='Primeros Auxilios')),
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_producto', models.CharField(default=b'-', max_length=30)),
                ('estado', models.IntegerField(default=1)),
                ('id_categoria', models.ForeignKey(default=0, to='helpmapp.Categoria')),
=======
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
=======
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
>>>>>>> 257318312f812d903fc2bead76200858d775501c
                ('nombre_producto', models.CharField(max_length=30, default='-')),
                ('estado', models.IntegerField(default=1)),
                ('id_categoria', models.ForeignKey(to='helpmapp.Categoria', default=0)),
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
            ],
        ),
        migrations.AddField(
            model_name='existenciainventario',
            name='id_producto',
<<<<<<< HEAD
            field=models.ForeignKey(default=0, to='helpmapp.Producto'),
=======
            field=models.ForeignKey(to='helpmapp.Producto', default=0),
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='id_centro',
<<<<<<< HEAD
            field=models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio'),
=======
            field=models.ForeignKey(to='helpmapp.CentroDeAcopio', default=0),
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='id_producto',
<<<<<<< HEAD
            field=models.ForeignKey(default=0, to='helpmapp.Producto'),
=======
            field=models.ForeignKey(to='helpmapp.Producto', default=0),
>>>>>>> 3fc867c08dc46e223069e541419fcfa7921e1034
        ),
    ]
