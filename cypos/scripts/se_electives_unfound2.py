from base.models import Majors, Courses, Electives
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def run():
    ip = []
    usd = []
    ah = []
    ss = []
    math = []
    econ = []
    see = []
    supp = []
    tech = []

    f = open("../files/degreeInfo/electives/txt/2unfound_international_electives.txt", "r")
    f2 = open("../files/degreeInfo/electives/txt/3unfound_international_electives.txt", "w")
    for line in f:
        ip.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f3 = open("../files/degreeInfo/electives/txt/2unfound_USD.txt", "r")
    f4 = open("../files/degreeInfo/electives/txt/3unfound_USD.txt", "w")
    for line in f3:
        usd.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f5 = open("../files/degreeInfo/electives/txt/2unfound_arts_&_humanities.txt", "r")
    f6 = open("../files/degreeInfo/electives/txt/3unfound_arts_&_humanities.txt", "w")
    for line in f5:
        ah.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f7 = open("../files/degreeInfo/electives/txt/2unfound_social_sciences.txt", "r")
    f8 = open("../files/degreeInfo/electives/txt/3unfound_social_sciences.txt", "w")
    for line in f7:
        ss.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f9 = open("../files/degreeInfo/electives/txt/2unfound_math_electives.txt", "r")
    f10 = open("../files/degreeInfo/electives/txt/3unfound_math_electives.txt", "w")
    for line in f9:
        math.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f11 = open("../files/degreeInfo/electives/txt/2unfound_econ_electives.txt", "r")
    f12 = open("../files/degreeInfo/electives/txt/3unfound_econ_electives.txt", "w")
    for line in f11:
        econ.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f13 = open("../files/degreeInfo/electives/txt/2unfound_software_engineering_electives.txt", "r")
    f14 = open("../files/degreeInfo/electives/txt/3unfound_software_engineering_electives.txt", "w")
    for line in f13:
        see.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f15 = open("../files/degreeInfo/electives/txt/2unfound_supp_electives.txt", "r")
    f16 = open("../files/degreeInfo/electives/txt/3unfound_supp_electives.txt", "w")
    for line in f15:
        supp.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f17 = open("../files/degreeInfo/electives/txt/2unfound_technical_electives.txt", "r")
    f18 = open("../files/degreeInfo/electives/txt/3unfound_technical_electives.txt", "w")
    for line in f17:
        tech.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    se = Majors.objects.get(name='Software Engineering')

    print("International Perspectives")
    elective = Electives.objects.get(name='International Perspective')
    for course in ip:
        try:
            c = Courses.objects.get(acronym=course)
            elective.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f2.write(course+"\n")
    elective.save()
    print("")

    print("US Diversity")
    elective2 = Electives.objects.get(name='U.S. Diversity', major=se)
    for course in usd:
        try:
            c = Courses.objects.get(acronym=course)
            elective2.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f4.write(course+"\n")
    elective2.save()
    print("")

    print("Arts and Humanities")
    elective3 = Electives.objects.get(name='Arts and Humanities', major=se)
    for course in ah:
        try:
            c = Courses.objects.get(acronym=course)
            elective3.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f6.write(course+"\n")
    elective3.save()
    print("")

    print("Social Sciences")
    elective4 = Electives.objects.get(name='Social Sciences', major=se)
    for course in ss:
        try:
            c = Courses.objects.get(acronym=course)
            elective4.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f8.write(course+"\n")
    elective4.save()
    print("")

    print("Arts and Humanities/Social Sciences")
    elective5 = Electives.objects.get(name='Arts and Humanities/Social Sciences', major=se)
    for course in ah:
        try:
            c = Courses.objects.get(acronym=course)
            elective5.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
    for course in ss:
        try:
            c = Courses.objects.get(acronym=course)
            elective5.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
    elective5.save()
    print("")

    print("Math Electives")
    elective6 = Electives.objects.get(name='Math', major=se)
    for course in math:
        try:
            c = Courses.objects.get(acronym=course)
            elective6.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f10.write(course+"\n")
    elective6.save()
    print("")

    print("Econ Electives")
    elective7 = Electives.objects.get(name='Econ', major=se)
    for course in econ:
        try:
            c = Courses.objects.get(acronym=course)
            elective7.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f12.write(course+"\n")
    elective7.save()
    print("")

    print("Software Engineering Electives")
    elective8 = Electives.objects.get(name='Software Engineering', major=se)
    for course in see:
        try:
            c = Courses.objects.get(acronym=course)
            elective8.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f14.write(course+"\n")
    elective8.save()
    print("")

    print("Supplemental Electives")
    elective9 = Electives.objects.get(name='Supplemental', major=se)
    for course in supp:
        try:
            c = Courses.objects.get(acronym=course)
            elective9.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f16.write(course+"\n")
    elective9.save()
    print("")

    print("Technical Electives")
    elective10 = Electives.objects.get(name='Technical', major=se)
    for course in tech:
        try:
            c = Courses.objects.get(acronym=course)
            elective10.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f18.write(course+"\n")
    elective10.save()
    print("")

    f.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    f10.close()
    f11.close()
    f12.close()
    f13.close()
    f14.close()
    f15.close()
    f16.close()
    f17.close()
    f18.close()
    print("Finished")