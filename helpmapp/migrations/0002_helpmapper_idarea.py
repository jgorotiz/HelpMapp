# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpmapper',
            name='idarea',
            field=models.ForeignKey(to='helpmapp.Area', default='-'),
        ),
    ]
