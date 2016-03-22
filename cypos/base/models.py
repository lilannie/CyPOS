from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TestDepartments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    acronym = models.TextField(null=False, blank=False)

    def __unicode__(self):
            return self.name


class TestCourses(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.TextField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    prereqs = models.ManyToManyField("self")
    numCredits = models.IntegerField(null=True, blank=False)
    department = models.ForeignKey(TestDepartments, null=True)

    def __unicode__(self):
        return self.number + " " + self.department.acronym


class Pos(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False)
    takenCourses = models.ManyToManyField(TestCourses, related_name='takenCourses', null=True)
    neededCourses = models.ManyToManyField(TestCourses, related_name='neededCourses', null=True)


class Majors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    department = models.ForeignKey(TestDepartments, null=True)
    reqCourses = models.ManyToManyField(TestCourses, null=True)


class Electives(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    department = models.ForeignKey(TestDepartments, null=True)
    major = models.ForeignKey(Majors, null=True)
    courses = models.ManyToManyField(TestCourses, null=True)


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









