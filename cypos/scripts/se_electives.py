from base.models import Majors, Courses, Electives
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def run():
    f = open("../files/degreeInfo/electives/txt/2international_electives_from_arts_&_humanities.txt", "r")
    courses = []
    for line in f:
        courses.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    se = Majors.objects.get(name='Software Engineering')
    elective = Electives.objects.create(name='International Perspective', major=se, creditNum=3)


    elective.save()
