# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0003_categoria_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='CambioInventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('tipo', models.IntegerField(default=1)),
                ('cantidad', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('idProducto', models.ForeignKey(to='helpmapp.Producto', default='-')),
            ],
        ),
    ]
