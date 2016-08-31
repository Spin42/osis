# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-28 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dissertation', '0003_dissertation_defend_periode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dissertation',
            name='defend_periode',
            field=models.CharField(choices=[('UNDEFINED', 'undefined'), ('JANUARY', 'January'), ('JUNE', 'June'), ('SEPTEMBER', 'September')], default='UNDEFINED', max_length=12),
        ),
    ]
