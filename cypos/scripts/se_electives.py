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

    f = open("../files/degreeInfo/software_engineering/electives/txt/international_electives_from_arts_&_humanities.txt", "r")
    f2 = open("../files/degreeInfo/software_engineering/electives/txt/international_electives_from_social_sciences.txt", "r")
    f3 = open("../files/degreeInfo/software_engineering/electives/txt/unfound_international_electives.txt", "w")
    for line in f:
        ip.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
        ah.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
    for line in f2:
        ip.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
        ss.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f4 = open("../files/degreeInfo/software_engineering/electives/txt/USD_from_arts_&_humanities.txt", "r")
    f5 = open("../files/degreeInfo/software_engineering/electives/txt/USD_from_social_sciences.txt", "r")
    f8 = open("../files/degreeInfo/software_engineering/electives/txt/unfound_USD.txt", "w")
    for line in f4:
        usd.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
        ah.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
    for line in f5:
        usd.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
        ss.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f6 = open("../files/degreeInfo/software_engineering/electives/txt/arts_&_humanities.txt", "r")
    f9 = open("../files/degreeInfo/software_engineering/electives/txt/unfound_arts_&_humanities.txt", "w")
    for line in f6:
        ah.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f7 = open("../files/degreeInfo/software_engineering/electives/txt/social_sciences.txt", "r")
    f10 = open("../files/degreeInfo/software_engineering/electives/txt/unfound_social_sciences.txt", "w")
    for line in f7:
        ss.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f11 = open("../files/degreeInfo/software_engineering/electives/txt/math_electives.txt", "r")
    f12 = open("../files/degreeInfo/software_engineering/electives/txt/unfound_math_electives.txt", "w")
    for line in f11:
        math.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f13 = open("../files/degreeInfo/software_engineering/electives/txt/econ_electives.txt", "r")
    f14 = open("../files/degreeInfo/software_engineering/electives/txt/unfound_econ_electives.txt", "w")
    for line in f13:
        econ.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f15 = open("../files/degreeInfo/software_engineering/electives/txt/software_engineering_electives.txt", "r")
    f16 = open("../files/degreeInfo/software_engineering/electives/txt/unfound_software_engineering_electives.txt", "w")
    for line in f15:
        see.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f17 = open("../files/degreeInfo/electives/txt/supp_electives.txt", "r")
    f18 = open("../files/degreeInfo/electives/txt/unfound_supp_electives.txt", "w")
    for line in f17:
        supp.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    f19 = open("../files/degreeInfo/software_engineering/electives/txt/technical_electives.txt", "r")
    f20 = open("../files/degreeInfo/software_engineering/electives/txt/unfound_technical_electives.txt", "w")
    for line in f19:
        tech.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    se = Majors.objects.get(name='Software Engineering')

    print("International Perspectives")
    elective = Electives.objects.create(name='International Perspective', major=se, creditNum=3)
    for course in ip:
        try:
            c = Courses.objects.get(acronym=course)
            elective.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f3.write(course+"\n")
    elective.save()
    print("")

    print("US Diversity")
    elective2 = Electives.objects.create(name='U.S. Diversity', major=se, creditNum=3)
    for course in usd:
        try:
            c = Courses.objects.get(acronym=course)
            elective2.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f8.write(course+"\n")
    elective2.save()
    print("")

    print("Arts and Humanities")
    elective3 = Electives.objects.create(name='Arts and Humanities', major=se, creditNum=6)
    for course in ah:
        try:
            c = Courses.objects.get(acronym=course)
            elective3.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f9.write(course+"\n")
    elective3.overlapWith.add(elective)
    elective3.overlapWith.add(elective2)
    elective3.save()
    print("")

    print("Social Sciences")
    elective4 = Electives.objects.create(name='Social Sciences', major=se, creditNum=6)
    for course in ss:
        try:
            c = Courses.objects.get(acronym=course)
            elective4.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f10.write(course+"\n")
    elective4.overlapWith.add(elective)
    elective4.overlapWith.add(elective2)
    elective4.save()
    print("")

    print("Arts and Humanities/Social Sciences")
    elective5 = Electives.objects.create(name='Arts and Humanities/Social Sciences', major=se, creditNum=6)
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
    elective5.overlapWith.add(elective)
    elective5.overlapWith.add(elective2)
    elective5.save()
    print("")

    print("Math Electives")
    elective6 = Electives.objects.create(name='Math', major=se, creditNum=3)
    for course in math:
        try:
            c = Courses.objects.get(acronym=course)
            elective6.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f12.write(course+"\n")
    elective6.save()
    print("")

    print("Econ Electives")
    elective7 = Electives.objects.create(name='Econ', major=se, creditNum=3)
    for course in econ:
        try:
            c = Courses.objects.get(acronym=course)
            elective7.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f14.write(course+"\n")
    elective7.save()
    print("")

    print("Software Engineering Electives")
    elective8 = Electives.objects.create(name='Software Engineering', major=se, creditNum=6)
    for course in see:
        try:
            c = Courses.objects.get(acronym=course)
            elective8.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f16.write(course+"\n")
    elective8.save()
    print("")

    print("Supplemental Electives")
    elective9 = Electives.objects.create(name='Supplemental', major=se, creditNum=9)
    for course in supp:
        try:
            c = Courses.objects.get(acronym=course)
            elective9.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f18.write(course+"\n")
    elective9.save()
    print("")

    print("Technical Electives")
    elective10 = Electives.objects.create(name='Technical', major=se, creditNum=9)
    for course in tech:
        try:
            c = Courses.objects.get(acronym=course)
            elective10.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f20.write(course+"\n")
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
    f19.close()
    f20.close()

    print("Finished")