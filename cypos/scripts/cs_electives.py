from base.models import Majors, Courses, Electives
from django.core.exceptions import ObjectDoesNotExist


def run():
    cs300 = []
    cs400g1 = []
    cs400g2 = []
    engl = []
    math = []
    ns = []
    nsadd = []
    stat = []
    ip = []
    usd = []
    ah = []
    ss = []

    fcs300 = open("../files/degreeInfo/computer_science/electives/txt/com_s_300.txt", "r")
    fcs300_uf = open("../files/degreeInfo/computer_science/electives/txt/com_s_300_unfound.txt", "w")
    for line in fcs300:
        cs300.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    fcs400g1 = open("../files/degreeInfo/computer_science/electives/txt/com_s_400_group_1.txt", "r")
    fcs400g1_uf = open("../files/degreeInfo/computer_science/electives/txt/com_s_400_group_1_unfound.txt", "w")
    for line in fcs400g1:
        cs400g1.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    fcs400g2 = open("../files/degreeInfo/computer_science/electives/txt/com_s_400_group_2.txt", "r")
    fcs400g2_uf = open("../files/degreeInfo/computer_science/electives/txt/com_s_400_group_2_unfound.txt", "w")
    for line in fcs400g2:
        cs400g2.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    fengl = open("../files/degreeInfo/computer_science/electives/txt/english.txt", "r")
    fengl_uf = open("../files/degreeInfo/computer_science/electives/txt/english_unfound.txt", "w")
    for line in fengl:
        engl.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    fmath = open("../files/degreeInfo/computer_science/electives/txt/math_option.txt", "r")
    fmath_uf = open("../files/degreeInfo/computer_science/electives/txt/math_option_unfound.txt", "w")
    for line in fmath:
        math.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    fns = open("../files/degreeInfo/computer_science/electives/txt/natural_science.txt", "r")
    fns_uf = open("../files/degreeInfo/computer_science/electives/txt/natural_science_unfound.txt", "w")
    for line in fns:
        ns.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    fnsadd = open("../files/degreeInfo/computer_science/electives/txt/natural_science_additional_requirement.txt", "r")
    fnsadd_uf = open("../files/degreeInfo/computer_science/electives/txt/natural_science_additional_requirement_unfound.txt", "w")
    for line in fnsadd:
        nsadd.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

    fstat = open("../files/degreeInfo/computer_science/electives/txt/statistic_option.txt", "r")
    fstat_uf = open("../files/degreeInfo/computer_science/electives/txt/statistic_option_unfound.txt", "w")
    for line in fstat:
        stat.append(line.replace("\t", " ").replace("\n", "").replace("\r", ""))

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
    f8 = open("../files/degreeInfo/software_engineering//electives/txt/unfound_USD.txt", "w")
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

    cs = Majors.objects.get(name='Computer Science')

    print("Computer Science 300 Level")
    e = Electives.objects.create(name='Computer Science 300 Level', major=cs, creditNum=6)
    for course in cs300:
        try:
            c = Courses.objects.get(acronym=course)
            e.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            fcs300_uf.write(course+"\n")
    e.save()
    print("")

    print("Computer Science 400 Level Group 1")
    e = Electives.objects.create(name='Computer Science 400 Level Group 1', major=cs, creditNum=6)
    for course in cs400g1:
        try:
            c = Courses.objects.get(acronym=course)
            e.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            fcs400g1_uf.write(course+"\n")
    e.save()
    print("")

    print("Computer Science 400 Level Group 2")
    e = Electives.objects.create(name='Computer Science 400 Level Group 2', major=cs, creditNum=6)
    for course in cs400g2:
        try:
            c = Courses.objects.get(acronym=course)
            e.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            fcs400g2_uf.write(course+"\n")
    e.save()
    print("")

    print("English")
    e = Electives.objects.create(name='English', major=cs, creditNum=3)
    for course in engl:
        try:
            c = Courses.objects.get(acronym=course)
            e.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            fengl_uf.write(course+"\n")
    e.save()
    print("")

    print("Math")
    e = Electives.objects.create(name='Math', major=cs, creditNum=3)
    for course in math:
        try:
            c = Courses.objects.get(acronym=course)
            e.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            fmath_uf.write(course+"\n")
    e.save()
    print("")

    print("Natural Sciences")
    e = Electives.objects.create(name='Natural Sciences', major=cs, creditNum=8)
    for course in ns:
        try:
            c = Courses.objects.get(acronym=course)
            e.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            fns_uf.write(course+"\n")
    e.save()
    print("")

    print("Natural Sciences Additional Requirement")
    e = Electives.objects.create(name='Natural Sciences Additional Requirement', major=cs, creditNum=3)
    for course in nsadd:
        try:
            c = Courses.objects.get(acronym=course)
            e.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            fnsadd_uf.write(course+"\n")
    e.save()
    print("")

    print("Statistic Electives")
    e = Electives.objects.create(name='Statistic', major=cs, creditNum=3)
    for course in stat:
        try:
            c = Courses.objects.get(acronym=course)
            e.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            fstat_uf.write(course+"\n")
    e.save()
    print("")

    print("Statistic Electives")
    e = Electives.objects.create(name='Statistic', major=cs, creditNum=3)
    for course in stat:
        try:
            c = Courses.objects.get(acronym=course)
            e.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            fstat_uf.write(course+"\n")
    e.save()
    print("")

    print("Arts and Humanities")
    eah = Electives.objects.create(name='Arts and Humanities', major=cs, creditNum=9)
    for course in ah:
        try:
            c = Courses.objects.get(acronym=course)
            eah.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f9.write(course+"\n")
    eah.save()
    print("")

    print("Social Sciences")
    ess = Electives.objects.create(name='Social Sciences', major=cs, creditNum=9)
    for course in ss:
        try:
            c = Courses.objects.get(acronym=course)
            ess.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f10.write(course+"\n")
    ess.save()
    print("")

    print("US Diversity")
    eusd = Electives.objects.create(name='US Diversity', major=cs, creditNum=3)
    for course in usd:
        try:
            c = Courses.objects.get(acronym=course)
            eusd.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f8.write(course+"\n")
    eusd.overlapWith.add(eah)
    eusd.overlapWith.add(ess)
    eusd.save()
    print("")

    print("International Perspective")
    eip = Electives.objects.create(name='International Perspective', major=cs, creditNum=3)
    for course in ip:
        try:
            c = Courses.objects.get(acronym=course)
            eip.courses.add(c)
        except ObjectDoesNotExist:
            print(course)
            f3.write(course+"\n")
    eip.overlapWith.add(eah)
    eip.overlapWith.add(ess)
    eip.save()
    print("")

    fcs300.close()
    fcs300_uf.close()
    fcs400g1.close()
    fcs400g1_uf.close()
    fcs400g2.close()
    fcs400g2_uf.close()
    fengl.close()
    fengl_uf.close()
    fmath.close()
    fmath_uf.close()
    fns.close()
    fns_uf.close()
    fnsadd.close()
    fnsadd_uf.close()
    fstat.close()
    fstat_uf.close()
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