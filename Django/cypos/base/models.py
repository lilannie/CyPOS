from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(null=False, blank=False)
    password = models.TextField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    firstname = models.TextField(null=False, blank=False)
    lastname = models.TextField(null=False, blank=False)


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.TextField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    prereqs = models.ManyToManyField("self")
    numCredits = models.IntegerField(null=False, blank=False)
    departmentID = models.ForeignKey(Departments, ond_delete=models.CASCADE, null=False)


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    acronym = models.TextField(null=False, blank=False)
    courses = models.ManyToOneRel(Courses)




