# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-14 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dissertation', '0006_auto_20160711_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dissertation',
            name='defend_periode',
            field=models.CharField(choices=[('UNDEFINED', 'undefined'), ('JANUARY', 'january'), ('JUNE', 'june'), ('SEPTEMBER', 'september')], default='UNDEFINED', max_length=12),
        ),
        migrations.AlterField(
            model_name='dissertation',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'draft'), ('DIR_SUBMIT', 'submitted_to_director'), ('DIR_OK', 'accepted_by_director'), ('DIR_KO', 'refused_by_director'), ('COM_SUBMIT', 'submitted_to_commission'), ('COM_OK', 'accepted_by_commission'), ('COM_KO', 'refused_by_commission'), ('EVA_SUBMIT', 'submitted_to_first_year_evaluation'), ('EVA_OK', 'accepted_by_first_year_evaluation'), ('EVA_KO', 'refused_by_first_year_evaluation'), ('TO_RECEIVE', 'to_be_received'), ('TO_DEFEND', 'to_be_defended'), ('DEFENDED', 'defended'), ('ENDED', 'ended'), ('ENDED_WIN', 'ended_win'), ('ENDED_LOS', 'ended_los')], default='DRAFT', max_length=12),
        ),
        migrations.AlterField(
            model_name='dissertationrole',
            name='status',
            field=models.CharField(choices=[('PROMOTEUR', 'pro'), ('CO_PROMOTEUR', 'popro'), ('READER', 'reader')], max_length=12),
        ),
        migrations.AlterField(
            model_name='dissertationupdate',
            name='status_from',
            field=models.CharField(choices=[('DRAFT', 'draft'), ('DIR_SUBMIT', 'submitted_to_director'), ('DIR_OK', 'accepted_by_director'), ('DIR_KO', 'refused_by_director'), ('COM_SUBMIT', 'submitted_to_commission'), ('COM_OK', 'accepted_by_commission'), ('COM_KO', 'refused_by_commission'), ('EVA_SUBMIT', 'submitted_to_first_year_evaluation'), ('EVA_OK', 'accepted_by_first_year_evaluation'), ('EVA_KO', 'refused_by_first_year_evaluation'), ('TO_RECEIVE', 'to_be_received'), ('TO_DEFEND', 'to_be_defended'), ('DEFENDED', 'defended'), ('ENDED', 'ended'), ('ENDED_WIN', 'ended_win'), ('ENDED_LOS', 'ended_los')], default='DRAFT', max_length=12),
        ),
        migrations.AlterField(
            model_name='dissertationupdate',
            name='status_to',
            field=models.CharField(choices=[('DRAFT', 'draft'), ('DIR_SUBMIT', 'submitted_to_director'), ('DIR_OK', 'accepted_by_director'), ('DIR_KO', 'refused_by_director'), ('COM_SUBMIT', 'submitted_to_commission'), ('COM_OK', 'accepted_by_commission'), ('COM_KO', 'refused_by_commission'), ('EVA_SUBMIT', 'submitted_to_first_year_evaluation'), ('EVA_OK', 'accepted_by_first_year_evaluation'), ('EVA_KO', 'refused_by_first_year_evaluation'), ('TO_RECEIVE', 'to_be_received'), ('TO_DEFEND', 'to_be_defended'), ('DEFENDED', 'defended'), ('ENDED', 'ended'), ('ENDED_WIN', 'ended_win'), ('ENDED_LOS', 'ended_los')], default='DRAFT', max_length=12),
        ),
        migrations.AlterField(
            model_name='offerproposition',
            name='end_visibility_dissertation',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='offerproposition',
            name='end_visibility_proposition',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='offerproposition',
            name='start_visibility_dissertation',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='offerproposition',
            name='start_visibility_proposition',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='propositionrole',
            name='status',
            field=models.CharField(choices=[('PROMOTEUR', 'pro'), ('CO_PROMOTEUR', 'copro'), ('READER', 'reader')], default='PROMOTEUR', max_length=12),
        ),
    ]