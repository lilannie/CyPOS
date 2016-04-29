from base.models import BasicProgram, Courses, Majors

def run():
    arr = ['CHEM 167', 'ENGL 150', 'ENGL 250', 'S E 101',
           'CPR E 185', 'LIB 160', 'MATH 165', 'MATH 166', 'PHYS 221']

    se = Majors.objects.get(name="Software Engineering")
    b = BasicProgram.objects.create(major=se)

    for course in arr:
        c = Courses.objects.get(acronym=course)
        b.courses.add(c)

    b.save()

