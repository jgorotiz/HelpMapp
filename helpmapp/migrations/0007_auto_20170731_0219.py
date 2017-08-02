# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0006_auto_20170731_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='id_Administrador',
            field=models.CharField(primary_key=True, max_length=16, serialize=False, default='-'),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='id_Centro',
            field=models.ForeignKey(to='helpmapp.CentroDeAcopio', default='-'),
        ),
        migrations.AlterField(
            model_name='cambioinventario',
            name='id_CambioInventario',
            field=models.CharField(primary_key=True, max_length=16, serialize=False, default='-'),
        ),
        migrations.AlterField(
            model_name='cambioinventario',
            name='id_producto',
            field=models.ForeignKey(to='helpmapp.Producto', default='-'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id_Categoria',
            field=models.CharField(primary_key=True, max_length=16, serialize=False, default='-'),
        ),
        migrations.AlterField(
            model_name='centrodeacopio',
            name='id_Centro',
            field=models.CharField(primary_key=True, max_length=16, serialize=False, default='-'),
        ),
        migrations.AlterField(
            model_name='habilidad',
            name='id_Habilidad',
            field=models.CharField(primary_key=True, max_length=16, serialize=False, default='-'),
        ),
        migrations.AlterField(
            model_name='habilidadhelpmapper',
            name='id_Habilidad',
            field=models.ForeignKey(to='helpmapp.Habilidad', default='-'),
        ),
        migrations.AlterField(
            model_name='habilidadhelpmapper',
            name='id_HabilidadHelpMapper',
            field=models.CharField(primary_key=True, max_length=16, serialize=False, default='-'),
        ),
        migrations.AlterField(
            model_name='habilidadhelpmapper',
            name='id_HelpMapper',
            field=models.ForeignKey(to='helpmapp.HelpMapper', default='-'),
        ),
        migrations.AlterField(
            model_name='helpmapper',
            name='id_HelpMapper',
            field=models.CharField(primary_key=True, max_length=16, serialize=False, default='-'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_Categoria',
            field=models.ForeignKey(to='helpmapp.Categoria', default='-'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_Centro',
            field=models.ForeignKey(to='helpmapp.CentroDeAcopio', default='-'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_Producto',
            field=models.CharField(primary_key=True, max_length=16, serialize=False, default='-'),
        ),
    ]
