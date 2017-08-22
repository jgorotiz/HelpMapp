# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0002_auto_20170820_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpmapper',
            name='estado',
            field=models.IntegerField(default=1),
        ),
    ]
