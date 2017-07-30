# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('package', models.CharField(max_length=50)),
                ('distributor', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('add_date', models.DateTimeField(verbose_name=b'date added')),
            ],
        ),
    ]
