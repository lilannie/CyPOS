from django.db import models


# Create your models here.
class TestUsers(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(null=False, blank=False)
    password = models.TextField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    firstname = models.TextField(null=False, blank=False)
    lastname = models.TextField(null=False, blank=False)


class TestDepartments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    acronym = models.TextField(null=False, blank=False)


class TestCourses(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.TextField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    prereqs = models.ManyToManyField("self")
    numCredits = models.IntegerField(null=False, blank=False)
    # departmentID = models.ForeignKey(TestDepartments, null=True, default=0)










