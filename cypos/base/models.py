from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Colleges(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)

    def __unicode__(self):
        return self.name


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    acronym = models.TextField(null=False, blank=False)
    college = models.ForeignKey(Colleges, null=True)

    def __unicode__(self):
        return self.name


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.TextField(null=False, blank=False, default='0')
    acronym = models.TextField(null=False, blank=False, default='0')
    name = models.TextField(null=False, blank=False, default='0')
    description = models.TextField(null=False, blank=False, default='0')
    prereqs = models.ManyToManyField("self")
    numCredits = models.IntegerField(null=True, blank=False, default='0')
    department = models.ForeignKey(Departments, null=True)

    def __unicode__(self):
        return self.number + " " + self.department.acronym


class Pos(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False)
    takenCourses = models.ManyToManyField(Courses, related_name='takenCourses')
    neededCourses = models.ManyToManyField(Courses, related_name='neededCourses')

    def __unicode__(self):
        return self.id


class Majors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    college = models.ForeignKey(Colleges, null=True)
    reqCourses = models.ManyToManyField(Courses)

    def __unicode__(self):
        return self.name


class Electives(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    major = models.ForeignKey(Majors, null=True)
    courses = models.ManyToManyField(Courses)

    def __unicode__(self):
        return self.id


class Substitutes(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, null=True)

    def __unicode__(self):
        return self.id









