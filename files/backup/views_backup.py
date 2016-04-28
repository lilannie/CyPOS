def pos_new(request):
    context = RequestContext(request)
    se = Majors.objects.get(name="Software Engineering")
    cpre = Majors.objects.get(name="Computer Engineering")
    cs = Majors.objects.get(name="Computer Science")
    majors = {se, cpre, cs}
    electives = Electives.objects.all()

    if request.method == 'POST':
        userMajor = Majors.objects.get(id=str(request.POST.get('major')))
        pos = Pos.objects.create(user=request.user, major=userMajor)

        electiveCourses = []
        electivesNeeded = []

        userElectives = Electives.objects.filter(major=userMajor)
        for elective in userElectives:
            posElective = PosElective.objects.create(pos=pos, elective=elective)
            creditsTaken = 0
            for course in elective.courses.all():
                if str(request.POST.get(str(course.id))) != 'None':
                    course = Courses.objects.get(acronym=request.POST.get(str(course.id)))
                    posElective.takenCourses.add(course)
                    creditsTaken = creditsTaken + int(course.numCredits)
                    electiveCourses.append(course)
            posElective.save()
            if(elective.creditNum - int(creditsTaken) < 0):
                posElective.creditsNeeded = 0
            else:
                posElective.creditsNeeded = elective.creditNum - int(creditsTaken)
                electivesNeeded.append(posElective)

        for reqCourse in userMajor.reqCourses.all():
            if str(request.POST.get(str(reqCourse.id))) != 'None':
                course = Courses.objects.get(acronym=request.POST.get(str(reqCourse.id)))
                pos.takenCourses.add(course)
            else:
                course = Courses.objects.get(id=reqCourse.id)
                pos.neededCourses.add(course)

        for course in electiveCourses:
            pos.takenCourses.add(course)

        pos.save()
        coursesNeeded = pos.neededCourses.all
        return render(request, 'base/view.html', {
            'pos': pos,
            'coursesNeeded': coursesNeeded,
            'electivesNeeded': electivesNeeded,
        }, context)

    return render(request, 'base/new.html', {
        'majors': majors,
        'electives': electives,
    })