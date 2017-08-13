# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0002_helpmapper_idarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombreCategoria', models.CharField(max_length=30)),
                ('unidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=30)),
                ('cantidad', models.DecimalField(default=0.0, decimal_places=2, max_digits=8)),
                ('idCategoria', models.ForeignKey(default='-', to='helpmapp.Categoria')),
            ],
        ),
    ]
