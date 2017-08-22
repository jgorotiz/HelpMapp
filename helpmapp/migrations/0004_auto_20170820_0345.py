# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0003_helpmapper_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpmapper',
            name='cedula',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='helpmapper',
            name='habilidad',
            field=models.CharField(default='Primeros Auxilios', max_length=30, choices=[('Primeros Auxilios', 'Primeros Auxilios'), ('Culinarias', 'Culinarias'), ('Trabajo de Campo', 'Trabajo de Campo')]),
        ),
        migrations.AlterField(
            model_name='helpmapper',
            name='nombreUsuario',
            field=models.CharField(default='-', max_length=18, serialize=False, primary_key=True),
        ),
    ]
