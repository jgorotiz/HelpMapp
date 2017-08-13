# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0004_cambioinventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('nombreUsuario', models.CharField(primary_key=True, max_length=12, serialize=False)),
                ('contrasena', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo', models.IntegerField(default=1)),
                ('estado', models.IntegerField(default=1)),
                ('idCentro', models.ForeignKey(default='-', to='helpmapp.CentroDeAcopio')),
            ],
        ),
    ]
