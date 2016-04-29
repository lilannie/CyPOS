# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-27 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_poselective_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='semesters',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='electives',
            name='courses',
            field=models.ManyToManyField(related_name='elective_courses', to='base.Courses'),
        ),
    ]