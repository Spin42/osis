# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-05 09:13
from __future__ import unicode_literals
from base.models.learning_unit import LearningUnit

from django.db import migrations


def remove_year_from_external_id(external_id):
    splitted_values = external_id.split('_')
    values_without_year = splitted_values[:-1]
    return '_'.join(values_without_year)


def update_external_id_field(apps, schema_editor):
    for learn_unit in LearningUnit.objects.raw('SELECT * FROM base_learningunit'):
        new_ext_id = remove_year_from_external_id(learn_unit.external_id)
        migrations.RunSQL("UPDATE base_learningunit set external_id = {} where external_id = {}"
                          .format(new_ext_id, learn_unit.external_id))


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0073_auto_20161028_0922'),
    ]

    operations = [
        migrations.RunPython(update_external_id_field),
    ]
