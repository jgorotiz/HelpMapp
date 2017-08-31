# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0003_auto_20170831_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='centrodeacopio',
            old_name='idAdmin',
            new_name='usuarioAdmin',
        ),
        migrations.RemoveField(
            model_name='cambioinventario',
            name='estado',
        ),
    ]
