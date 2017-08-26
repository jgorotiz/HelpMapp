# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0004_auto_20170820_0345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='helpmapper',
            old_name='nombreUsuario',
            new_name='nombre_usuario',
        ),
        migrations.RenameField(
            model_name='helpmapper',
            old_name='tipoSangre',
            new_name='tipo_sangre',
        ),
    ]
