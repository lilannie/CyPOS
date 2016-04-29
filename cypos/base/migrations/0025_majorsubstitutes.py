# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_basicprogram_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='MajorSubstitutes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MajorSubstitutesCourse', to='base.Courses')),
                ('courseFor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MajorSubstitutesCourseFor', to='base.Courses')),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MajorSubstitute', to='base.Majors')),
            ],
        ),
    ]
