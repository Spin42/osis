# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-01 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0010_remove_internshipenrollment_learning_unit_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipmaster',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='internship.Organization'),
        ),
    ]
