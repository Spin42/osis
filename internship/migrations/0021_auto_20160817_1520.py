# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-17 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0020_internshipspeciality_acronym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipstudentaffectationstat',
            name='choice',
            field=models.CharField(default='0', max_length=1),
        ),
    ]