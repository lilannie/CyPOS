# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_testcourses_departmentid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcourses',
            old_name='departmentID',
            new_name='department',
        ),
    ]
