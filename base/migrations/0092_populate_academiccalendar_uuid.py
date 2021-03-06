# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-05 09:13
from __future__ import unicode_literals
from django.db import migrations
import uuid


def set_uuids_model(apps, model):
    base = apps.get_app_config('base')
    model_class = base.get_model(model)
    ids = model_class.objects.values_list('id', flat=True)
    if ids:
        for pk in ids:
            model_class.objects.filter(pk=pk).update(uuid=uuid.uuid4())


def set_uuid_field(apps, schema_editor):
    set_uuids_model(apps, "academiccalendar")


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0091_academiccalendar_uuid'),
    ]

    operations = [
        migrations.RunPython(set_uuid_field),
    ]
