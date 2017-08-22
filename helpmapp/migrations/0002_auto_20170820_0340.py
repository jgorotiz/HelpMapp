# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpmapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpmapper',
            name='estado',
        ),
        migrations.AlterField(
            model_name='helpmapper',
            name='cedula',
            field=models.CharField(max_length=10, default='M'),
        ),
        migrations.AlterField(
            model_name='helpmapper',
            name='sexo',
            field=models.CharField(max_length=5, choices=[('M', 'M'), ('F', 'F')], default='M'),
        ),
    ]
