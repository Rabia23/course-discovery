# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0050_auto_20170524_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_metadata_pk',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Course Metadata Course PK'),
        ),
        migrations.AddField(
            model_name='historicalcourse',
            name='course_metadata_pk',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Course Metadata Course PK'),
        ),
    ]
