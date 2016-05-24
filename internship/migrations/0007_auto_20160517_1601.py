# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-17 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0006_auto_20160517_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipchoice',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.Organization'),
        ),
        migrations.AlterField(
            model_name='internshipmaster',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.Organization'),
        ),
        migrations.AlterField(
            model_name='internshipoffer',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.Organization'),
        ),
    ]