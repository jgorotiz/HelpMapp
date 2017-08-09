# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('idCentro', models.CharField(primary_key=True, default='-', serialize=False, max_length=16)),
                ('nombreUPC', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('latitud', models.DecimalField(max_digits=15, default=0.0, decimal_places=10)),
                ('longitud', models.DecimalField(max_digits=15, default=0.0, decimal_places=10)),
                ('provincia', models.CharField(max_length=30)),
                ('canton', models.CharField(max_length=30)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('idHabilidad', models.CharField(primary_key=True, default='-', serialize=False, max_length=16)),
                ('nombreHabilidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('idHelpMapper', models.CharField(primary_key=True, default='-', serialize=False, max_length=16)),
                ('nombreUsuario', models.CharField(max_length=12)),
                ('contrasena', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=100)),
                ('estado', models.IntegerField(default=1)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('tipoSangre', models.CharField(max_length=5)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
    ]
