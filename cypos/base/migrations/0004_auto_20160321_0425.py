# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20160321_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcourses',
            name='numCredits',
            field=models.IntegerField(null=True),
        ),
    ]
