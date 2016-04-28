from base.models import Majors, Semesters, Courses, Electives, FourYrPlan
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def run():
    s1 = ['MATH 165', 'ENGL 150', 'S E 101', 'LIB 160', 'CHEM 167', 'S E 185']
    s2 = ['COM S 227', 'MATH 166', 'S E 166', 'PHYS 221', {'Elective': 'Econ'}]
    s3 = ['CPR E 281', 'ENGL 250', 'MATH 267', 'COM S 228', 'SP CM 212']
    s4 = [{'Elective': 'Arts and Humanities'}, {'Elective': 'Math'},
          'COM S 327', 'COM S 363']
    s5 = [{'Elective': 'Arts and Humanities'}, 'S E 319', 'COM S 309',
          'COM S 230', 'COM S 321']
    s6 = [{'Elective': 'Arts and Humanities/Social Sciences'}, 'S E 339',
          'S E 329', 'COM S 311', 'COM S 352', 'ENGL 314']
    s7 = [{'Elective': 'Social Sciences'}, {'Elective': 'Technical'},
          {'Elective': 'Software Engineering'}, 'STAT 330', 'S E 491', 'S E 494']
    s8 = [{'Elective': 'Arts and Humanities/Social Sciences'}, {'Elective': 'Software Engineering'},
          {'Elective': 'Supplemental'}, {'Elective': 'Supplemental'}, {'Elective': 'Supplemental'}, 'S E 492']
    sems = [s1, s2, s3, s4, s5, s6, s7, s8]

    se = Majors.objects.get(name="Software Engineering")
    plan = FourYrPlan.objects.create(major=se)

    order = 0
    for semester in sems:
        numCredits = 0
        s = Semesters.objects.create(order=order)
        for course in semester:
            if(isinstance(course, dict)):
                try:
                    elective = Electives.objects.get(name=course.get('Elective'))
                    numCredits += 3
                    s.electives.add(elective)
                except:
                    print(course)
            else:
                try:
                    c = Courses.objects.get(acronym=course)
                    try:
                        numCredits += int (c.numCredits)
                    except ValueError:
                        numCredits = numCredits
                    s.courses.add(c)
                except ObjectDoesNotExist:
                    print(course)
        s.numCredits = numCredits
        s.save()
        plan.semesters.add(s)
        order += 1

    plan.save()
