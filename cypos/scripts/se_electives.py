from base.models import Majors, Courses, Electives
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def run():
    f = open("../files/degreeInfo/electives/txt/international_electives_from_arts_&_humanities.txt", "r")
    f2 = open("../files/degreeInfo/electives/txt/international_electives_from_social_sciences.txt", "r")
    f3 = open("../files/degreeInfo/electives/txt/unfound_international_electives.txt", "w")

    f4 = open("../files/degreeInfo/electives/txt/USD_from_arts_&_humanities.txt", "r")
    f5 = open("../files/degreeInfo/electives/txt/USD_from_social_sciences.txt", "r")
    f8 = open("../files/degreeInfo/electives/txt/unfound_USD.txt", "w")

    f6 = open("../files/degreeInfo/electives/txt/arts_&_humanities.txt", "r")
    f9 = open("../files/degreeInfo/electives/txt/unfound_arts_&_humanities.txt", "w")

    f7 = open("../files/degreeInfo/electives/txt/social_sciences.txt", "r")
    f10 = open("../files/degreeInfo/electives/txt/unfound_social_sciences.txt", "w")

    f11 = open("../files/degreeInfo/electives/txt/math_electives.txt", "r")
    f12 = open("../files/degreeInfo/electives/txt/unfound_math_electives.txt", "w")

    ip = []
    usd = []
    ah = []
    ss = []
    math = []

    for line in f:
        ip.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
        ah.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
    for line in f2:
        ip.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
        ss.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    for line in f4:
        usd.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
        ah.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
    for line in f5:
        usd.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))
        ss.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    for line in f6:
        ah.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    for line in f7:
        ss.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    for line in f11:
        math.append(line.replace("\t", "").replace("\n", "").replace("\r", ""))

    se = Majors.objects.get(name='Software Engineering')

    print("International Perspectives")
    elective = Electives.objects.create(name='International Perspective', major=se, creditNum=3)
    for course in ip:
        try:
            c = Courses.objects.get(acronym=course)
            elective.courses.add(c)
        except:
            print(course)
            f3.write(course+"\n")
    elective.save()

    print("US Diversity")
    elective2 = Electives.objects.create(name='U.S. Diversity', major=se, creditNum=3)
    for course in usd:
        try:
            c = Courses.objects.get(acronym=course)
            elective2.courses.add(c)
        except:
            print(course)
            f8.write(course+"\n")
    elective2.save()

    print("Arts and Humanities")
    elective3 = Electives.objects.create(name='Arts and Humanities', major=se, creditNum=6)
    for course in ah:
        try:
            c = Courses.objects.get(acronym=course)
            elective3.courses.add(c)
        except:
            print(course)
            f9.write(course+"\n")
    elective3.overlapWith.add(elective)
    elective3.overlapWith.add(elective2)
    elective3.save()

    print("Social Sciences")
    elective4 = Electives.objects.create(name='Social Sciences', major=se, creditNum=6)
    for course in ss:
        try:
            c = Courses.objects.get(acronym=course)
            elective4.courses.add(c)
        except:
            print(course)
            f10.write(course+"\n")
    elective4.overlapWith.add(elective)
    elective4.overlapWith.add(elective2)
    elective4.save()

    print("Arts and Humanities/Social Sciences")
    elective5 = Electives.objects.create(name='Arts and Humanities/Social Sciences', major=se, creditNum=6)
    for course in ah:
        try:
            c = Courses.objects.get(acronym=course)
            elective5.courses.add(c)
        except:
            print(course)
    for course in ss:
        try:
            c = Courses.objects.get(acronym=course)
            elective5.courses.add(c)
        except:
            print(course)
    elective5.overlapWith.add(elective)
    elective5.overlapWith.add(elective2)
    elective5.save()

    print("Math Electives")
    elective6 = Electives.objects.create(name='Math', major=se, creditNum=3)
    for course in math:
        try:
            c = Courses.objets.get(acronym=course)
            elective6.courses.add(c)
        except:
            print(course)
            f12.write(course+"\n")
    elective6.save()



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

    print("Finished")


