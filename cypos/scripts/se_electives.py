from base.models import Majors, Courses, Electives
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def run():
    se = Majors.objects.get(name='Software Engineering')
    count = 0
    elective = Electives.objects.create(name='International Perspective', major=se, creditNum=3)
    elective.save()
