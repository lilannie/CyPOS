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
    college = models.ForeignKey(Colleges, null=True, on_delete=models.CASCADE())

    def __unicode__(self):
        return self.name


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.TextField(null=False, blank=False, default='0')
    acronym = models.TextField(null=False, blank=False, default='0')
    name = models.TextField(null=False, blank=False, default='0')
    description = models.TextField(null=False, blank=False, default='0')
    # prereqs = models.ManyToManyField("self", on_delete=models.SET_NULL())
    numCredits = models.IntegerField(null=True, blank=False, default='0')
    department = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE())
    classificationNeeded = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return self.number + " " + self.department.acronym


class Prerequisite(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE())
    courseFor = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE())
    NONE = 'N'
    FRESHMAN = 'F'
    SOPHOMORE = 'SP'
    JUNIOR = 'J'
    SENIOR = 'S'
    CLASSIFICATION_CHOICES = (
        (NONE, 'None')
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    classification = CLASSIFICATION_CHOICES


class Corequisite(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE())
    courseFor = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE())


class Semesters(models.Model):
    id = models.AutoField(primary_key=True)
    numCredits = models.IntegerField(null=True, blank=True, default='0')
    SPRING = 'S'
    SUMMER = 'SS'
    FALL = 'F'
    TERM_CHOICES = (
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
        (FALL, 'Fall'),
    )
    term = TERM_CHOICES
    courses = models.ManyToManyField(Courses, related_name='courses', null=True, on_delete=models.SET_NULL())


class Majors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    college = models.ForeignKey(Colleges, null=True, on_delete=models.CASCADE())
    reqCourses = models.ManyToManyField(Courses, null=True, on_delete=models.SET_NULL())

    def __unicode__(self):
        return self.name


class Pos(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE())
    major = models.ForeignKey(Majors, null=True, on_delete=models.CASCADE())
    takenCourses = models.ManyToManyField(Courses, related_name='takenCourses', on_delete=models.SET_NULL())
    neededCourses = models.ManyToManyField(Courses, related_name='neededCourses', on_delete=models.SET_NULL())
    semesters = models.ManyToManyField(Semesters, related_name='semesters', on_delete=models.SET_NULL())

    def __unicode__(self):
        return self.id


class Electives(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    major = models.ForeignKey(Majors, null=True, on_delete=models.CASCADE())
    courses = models.ManyToManyField(Courses, null=True, on_delete=models.SET_NULL())

    def __unicode__(self):
        return self.id


class Substitutes(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE())
    preqFor = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE())

    def __unicode__(self):
        return self.id









