# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0004_auto_20170820_0345'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExistenciaInventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('idCentro', models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='idCentro',
            field=models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio'),
        ),
        migrations.AddField(
            model_name='existenciainventario',
            name='idProducto',
            field=models.ForeignKey(default=0, to='helpmapp.Producto'),
        ),
    ]
