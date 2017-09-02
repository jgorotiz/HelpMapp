# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0002_auto_20170831_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cambioinventario',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
