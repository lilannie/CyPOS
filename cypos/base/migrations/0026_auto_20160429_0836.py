# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_majorsubstitutes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fouryrplan',
            name='major',
        ),
        migrations.RemoveField(
            model_name='fouryrplan',
            name='semesters',
        ),
        migrations.DeleteModel(
            name='FourYrPlan',
        ),
    ]
