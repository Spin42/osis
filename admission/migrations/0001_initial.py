# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-06 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0027_auto_20160406_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('offer_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.OfferYear')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('value', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('LABEL', 'Label'), ('SHORT_INPUT_TEXT', 'Short input text'), ('LONG_INPUT_TEXT', 'Long input text'), ('RADIO_BUTTTON', 'Radio button'), ('CHECKBOX', 'Checkbox'), ('DROPDOWN_LIST', 'Dropdown list'), ('UPLOAD_BUTTON', 'Upload button'), ('DOWNLOAD_LINK', 'Download link'), ('HTTP_LINK', 'HTTP link')], max_length=20)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('required', models.BooleanField(default=False)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.Form')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.Question'),
        ),
    ]
