from cypos.base.models import Majors, Departments, Courses

fnumbers = open('./database_population/txt/se_courses_numbers.txt', 'r')
fdepartments = open('./database_population/txt/se_courses_depart.txt', 'r')

se = Majors.objects.get(name="Software Engineering")
for line in fnumbers:
    acronym = fdepartments.readline()
    depart = Departments.object.get(acronym="acronym")
    course = Courses(number=line, department_id=depart, acronym=acronym+line)
    course.save()
    se.reqCourses.add(course)