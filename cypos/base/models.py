from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    acronym = models.TextField(null=False, blank=False)

    def __unicode__(self):
            return self.name


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.TextField(null=False, blank=False)
    acronym = models.TextField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    prereqs = models.ManyToManyField("self")
    numCredits = models.IntegerField(null=True, blank=False)
    department = models.ForeignKey(Departments, null=True)

    def __unicode__(self):
        return self.number + " " + self.department.acronym


class Pos(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False)
    takenCourses = models.ManyToManyField(Courses, related_name='takenCourses')
    neededCourses = models.ManyToManyField(Courses, related_name='neededCourses')


class Majors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    department = models.ForeignKey(Departments, null=True)
    reqCourses = models.ManyToManyField(Courses)


class Electives(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    department = models.ForeignKey(Departments, null=True)
    major = models.ForeignKey(Majors, null=True)
    courses = models.ManyToManyField(Courses)


# class UserProfile(models.Model):
#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User)
#
#     # The additional attributes we wish to include.
#     website = models.URLField(blank=True)
#     # picture = models.ImageField(upload_to='profile_images', blank=True)
#
#     # Override the __unicode__() method to return out something meaningful!
#     def __unicode__(self):
#         return self.user.username









