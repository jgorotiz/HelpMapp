# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='component',
            name='category',
        ),
        migrations.RemoveField(
            model_name='component',
            name='distributor',
        ),
        migrations.RemoveField(
            model_name='component',
            name='package',
        ),
        migrations.RemoveField(
            model_name='component',
            name='place',
        ),
        migrations.RemoveField(
            model_name='component',
            name='price',
        ),
        migrations.RemoveField(
            model_name='component',
            name='quantity',
        ),
    ]
