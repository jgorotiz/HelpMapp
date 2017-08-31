# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0002_auto_20170831_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centrodeacopio',
            name='idAdmin',
            field=models.ForeignKey(default='-', to='helpmapp.Administrador'),
        ),
    ]
