from base.models import Majors, Departments, Courses
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def run():
    numbers = ['165', '167', '101', '185', '160', '150', '166', '221', '227', '166', '267', '212', '228', '281', '250',
                '327', '363', '319', '309', '230', '321', '339', '329', '311', '352', '314', '330', '491', '494', '492']
    departments = ['MATH', 'CHEM', 'S E', 'CPR E', 'LIB', 'ENGL', 'MATH', 'PHYS', 'COM S', 'S E', 'Math', 'SP CM', 'COM S',
                    'CPR E', 'ENGL', 'COM S',
                    'COM S', 'S E', 'COM S', 'COM S', 'COM S', 'S E', 'S E', 'COM S', 'COM S', 'ENGl', 'STAT', 'S E', 'S E', 'S E']
    se = Majors.objects.get(name='Software Engineering')
    count = 0
    for number in numbers:
        try:
            course = Courses.objects.get(acronym=departments[count].upper()+" "+numbers[count])
            se.reqCourses.add(course)
        except ObjectDoesNotExist:
            print("ObjectDoesNotExist: "+departments[count].upper()+" "+numbers[count])
        except MultipleObjectsReturned:
            print("MultipleObjects Returned: "+departments[count].upper()+" "+numbers[count])

        count += 1
    print("finished")