# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0005_auto_20170731_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='id_Administrador',
            field=models.CharField(serialize=False, max_length=16, default='', primary_key=True),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='id_Centro',
            field=models.ForeignKey(default='', to='helpmapp.CentroDeAcopio'),
        ),
        migrations.AlterField(
            model_name='cambioinventario',
            name='id_CambioInventario',
            field=models.CharField(serialize=False, max_length=16, default='', primary_key=True),
        ),
        migrations.AlterField(
            model_name='cambioinventario',
            name='id_producto',
            field=models.ForeignKey(default='', to='helpmapp.Producto'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id_Categoria',
            field=models.CharField(serialize=False, max_length=16, default='', primary_key=True),
        ),
        migrations.AlterField(
            model_name='centrodeacopio',
            name='id_Centro',
            field=models.CharField(serialize=False, max_length=16, default='', primary_key=True),
        ),
        migrations.AlterField(
            model_name='habilidad',
            name='id_Habilidad',
            field=models.CharField(serialize=False, max_length=16, default='', primary_key=True),
        ),
        migrations.AlterField(
            model_name='habilidadhelpmapper',
            name='id_Habilidad',
            field=models.ForeignKey(default='', to='helpmapp.Habilidad'),
        ),
        migrations.AlterField(
            model_name='habilidadhelpmapper',
            name='id_HabilidadHelpMapper',
            field=models.CharField(serialize=False, max_length=16, default='', primary_key=True),
        ),
        migrations.AlterField(
            model_name='habilidadhelpmapper',
            name='id_HelpMapper',
            field=models.ForeignKey(default='', to='helpmapp.HelpMapper'),
        ),
        migrations.AlterField(
            model_name='helpmapper',
            name='id_HelpMapper',
            field=models.CharField(serialize=False, max_length=16, default='', primary_key=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_Categoria',
            field=models.ForeignKey(default='', to='helpmapp.Categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_Centro',
            field=models.ForeignKey(default='', to='helpmapp.CentroDeAcopio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_Producto',
            field=models.CharField(serialize=False, max_length=16, default='', primary_key=True),
        ),
    ]
