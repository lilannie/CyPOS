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
    college = models.ForeignKey(Colleges, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.name


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.TextField(null=False, blank=False, default='0')
    acronym = models.TextField(null=False, blank=False, default='0')
    name = models.TextField(null=False, blank=False, default='0')
    description = models.TextField(null=False, blank=False, default='0')
    numCredits = models.IntegerField(null=True, blank=False, default='0')
    department = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE)
    classificationNeeded = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return self.department.acronym + " " + self.number


class Prerequisite(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE, related_name='prerequisite_course')
    courseFor = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE, related_name='prerequisite_courseFor')


class Corequisite(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE, related_name='corequisite_course')
    courseFor = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE, related_name='corequisite_courseFor')


class Majors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    college = models.ForeignKey(Colleges, null=True, on_delete=models.CASCADE)
    reqCourses = models.ManyToManyField(Courses)

    def __unicode__(self):
        return self.name


class Electives(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, blank=False)
    major = models.ForeignKey(Majors, null=True, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Courses, related_name="elective_courses")
    creditNum = models.IntegerField(null=True, blank=True)
    overlapWith = models.ManyToManyField("self")

    def __unicode__(self):
        return self.name


class Semesters(models.Model):
    id = models.AutoField(primary_key=True)
    numCredits = models.IntegerField(null=True, blank=True, default='0')
    courses = models.ManyToManyField(Courses, related_name='courses')
    order = models.IntegerField(null=True, blank=True)
    electives = models.ManyToManyField(Electives, related_name='electives_in_semester')

    def __unicode__(self):
        return self.id


class Pos(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    major = models.ForeignKey(Majors, null=True, on_delete=models.CASCADE)
    takenCourses = models.ManyToManyField(Courses, related_name='takenCourses')
    neededCourses = models.ManyToManyField(Courses, related_name='neededCourses')
    semesters = models.ManyToManyField(Semesters, related_name='semesters')

    def __unicode__(self):
        return self.id

class BasicProgram(models.Model):
    id = models.AutoField(primary_key=True)
    major = models.ForeignKey(Majors, related_name='BasicProgramMajor', null=True,on_delete=models.CASCADE)
    courses = models.ManyToManyField(Courses, related_name="BasicProgramCourses")


class PosElective(models.Model):
    id = models.AutoField(primary_key=True)
    pos = models.ForeignKey(Pos, null=True, on_delete=models.CASCADE)
    elective = models.ForeignKey(Electives, null=True, on_delete=models.CASCADE)
    takenCourses = models.ManyToManyField(Courses, related_name='elective_takenCourses')
    creditsNeeded = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.elective.name


class Substitutes(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE, related_name='substitute_course')
    courseFor = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE, related_name='substitute_courseFor')
    courseSubOf = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE, related_name='substitude_courseSubOf')

    def __unicode__(self):
        return self.id


class Password(models.Model):
    id = models.AutoField(primary_key=True)
    old_password = models.TextField(null=False, blank=False)
    new_password_1 = models.TextField(null=False, blank=False)
    new_password_2 = models.TextField(null=False, blank=False)

    def __unicode__(self):
        return self.id

# Class to be used with Haystack Search
class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title

class MajorSubstitutes(models.Model):
    id = models.AutoField(primary_key=True)
    major = models.ForeignKey(Majors, related_name='MajorSubstitute', null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE, related_name='MajorSubstitutesCourse')
    courseFor = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE, related_name='MajorSubstitutesCourseFor')





