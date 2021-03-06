# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 07:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0023_substitutes_coursesubof'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicProgram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('courses', models.ManyToManyField(related_name='BasicProgramCourses', to='base.Courses')),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BasicProgramMajor', to='base.Majors')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
