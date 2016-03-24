from base.models import Majors, Departments, Courses
from django.core.exceptions import ObjectDoesNotExist


def run():
    fnumbers = ['165', '167', '101', '185', '160', '150', '166', '221', '227', '166', '267', '212', '228', '281', '250',
                '229', '363', '319', '309', '330', '321', '339', '329', '311', '352', '314', '330', '491', '494', '492']
    fdepartments = ['Math', 'Chem', 'SE', 'CprE', 'Lib', 'Engl', 'Math', 'Phys', 'ComS', 'SE', 'Math', 'SpCm', 'ComS',
                    'CprE', 'Engl', 'ComS',
                    'ComS', 'SE', 'ComS', 'ComS', 'ComS', 'SE', 'SE', 'ComS', 'ComS', 'Engl', 'Stat', 'SE', 'SE', 'SE']
    se = Majors.objects.get(name="Software Engineering")
    count = 0
    for number in fnumbers:
        try:
            depart = Departments.objects.get(acronym=fdepartments[count])
            course = Courses(number=number, department_id=depart.id, acronym=fdepartments[count]+" "+number)
            course.save()
            se.reqCourses.add(course)
        except ObjectDoesNotExist:
            print("depart object unsuccessful: "+fdepartments[count])
        count += 1
    print("finished")