# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('idarea', models.CharField(serialize=False, default='-', primary_key=True, max_length=16)),
                ('nombre', models.CharField(default='-', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('idCentro', models.CharField(serialize=False, default='-', primary_key=True, max_length=16)),
                ('nombreUPC', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('latitud', models.DecimalField(max_digits=15, decimal_places=10, default=0.0)),
                ('longitud', models.DecimalField(max_digits=15, decimal_places=10, default=0.0)),
                ('provincia', models.CharField(max_length=30)),
                ('canton', models.CharField(max_length=30)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('idHelpMapper', models.CharField(serialize=False, default='-', primary_key=True, max_length=16)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nombreUsuario', models.CharField(max_length=12)),
                ('contrasena', models.CharField(max_length=15)),
                ('sexo', models.CharField(max_length=10)),
                ('cedula', models.CharField(max_length=10)),
                ('tipoSangre', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='O+', max_length=5)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=100)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
