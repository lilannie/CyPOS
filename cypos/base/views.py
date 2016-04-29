from django.shortcuts import render
from .forms import UserForm, UserEditForm, ChangePasswordForm
from .models import Courses, Majors, Pos, Electives, Departments, \
    Colleges, PosElective, Prerequisite, Corequisite, \
    Substitutes, BasicProgram, Semesters
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.auth.models import User


def register(request):
    # Like before, get the request's context.
    context = RequestContext (request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm (data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid ():
            # Save the user's form data to the database.
            user = user_form.save ()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password (user.password)
            user.save ()
            user = authenticate (username=request.POST.get ('username'), password=request.POST.get ('password'))
            login (request, user)
            # Update our variable to tell the template registration was successful.

            return render (request, 'base/home.html', {}, context)

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm ()

    # Render the template depending on the context.
    return render (request, 'base/register.html', {'user_form': user_form, 'registered': registered}, context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext (request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate (username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login (request, user)
                return render (request, 'base/home.html', {}, context)
            else:
                # An inactive account was used - no logging in!
                return render (request, 'base/index.html', {}, context)
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format (username, password))
            return render (request, 'base/index.html', {}, context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render (request, 'base/index.html', {}, context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout (request)

    # Take the user back to the homepage.
    return render (request, 'base/index.html', {})


def courses_view(request):
    departments = Departments.objects.all ()
    ag = []
    bus = []
    des = []
    eng = []
    grad = []
    hs = []
    las = []
    vet = []

    for department in departments:
        if department.college_id == 1:
            ag.append (department)
        elif department.college_id == 2:
            bus.append (department)
        elif department.college_id == 3:
            des.append (department)
        elif department.college_id == 4:
            eng.append (department)
        elif department.college_id == 5:
            grad.append (department)
        elif department.college_id == 6:
            hs.append (department)
        elif department.college_id == 7:
            las.append (department)
        elif department.college_id == 8:
            vet.append (department)

    return render (request, 'base/courses.html', {
        'ag': ag,
        'bus': bus,
        'des': des,
        'eng': eng,
        'grad': grad,
        'hs': hs,
        'las': las,
        'vet': vet,
    })


def course_view_department(request, id):
    try:
        courses = Courses.objects.filter (department_id=id).order_by ('number')
        department = Departments.objects.get (id=id)
    except Courses.DoesNotExist:
        courses = []
        department = []
    return render (request, 'base/course_department.html', {
        'courses': courses,
        'department': department,
    })


def user_help(request):
    return render (request, 'base/help.html')


def pos_history(request):
    return render (request, 'base/history.html')


def home(request):
    return render (request, 'base/home.html')


def user_manage(request):
    user = request.user
    try:
        pos = Pos.objects.filter (user=request.user).order_by ('-id')[0]
        takenCourses = pos.takenCourses.all ()
    except:
        pos = []
        takenCourses = []
    return render (request, 'base/manage.html', {
        'user': user,
        'pos': pos,
        'takenCourses': takenCourses
    })


def pos_new(request):
    context = RequestContext (request)
    se = Majors.objects.get (name="Software Engineering")
    cpre = Majors.objects.get (name="Computer Engineering")
    cs = Majors.objects.get (name="Computer Science")
    majors = {se}
    electives = Electives.objects.all ()

    if request.method == 'POST':
        if str (request.path_info) == '/new':
            userMajor = Majors.objects.get (id=str (request.POST.get ('major')))
            pos = Pos.objects.create (user=request.user, major=userMajor)
            pos.save ()
            electivesNeeded = []

            userElectives = Electives.objects.filter (major=userMajor)
            for elective in userElectives:
                posElective = PosElective.objects.create (pos=pos, elective=elective)
                creditsTaken = 0
                coursesTaken = request.POST.getlist (str (elective.id) + "elective")
                for course in coursesTaken:
                    c = Courses.objects.get (id=course)
                    # print("Found "+str(c)+" for "+str(elective))
                    posElective.takenCourses.add (c)
                    creditsTaken = creditsTaken + int (c.numCredits)
                    pos.takenCourses.add (c)

                posElective.save ()

                if (elective.creditNum - int (creditsTaken) < 0):
                    posElective.creditsNeeded = 0
                else:
                    posElective.creditsNeeded = elective.creditNum - int (creditsTaken)
                    if posElective.creditsNeeded != 0:
                        electivesNeeded.append (posElective)

            coursesTaken = request.POST.getlist (str (userMajor.id) + "major")
            for course in coursesTaken:
                c = Courses.objects.get (acronym=course)
                pos.takenCourses.add (c)

            for reqCourse in userMajor.reqCourses.all ():
                if reqCourse.acronym not in coursesTaken:
                    pos.neededCourses.add (reqCourse)

            if (len (electivesNeeded) == 0):
                return render (request, 'base/new_check_prereq.html', {
                    'pos': pos,
                }, context)
            else:
                return render (request, 'base/new_check.html', {
                    'posId': pos.id,
                    'electivesNeeded': electivesNeeded,
                    'userMajorId': request.POST.get ('major'),
                }, context)

        elif str (request.path_info) == '/newcheck':
            userMajor = Majors.objects.get (id=str (request.POST.get ('major')))
            userElectives = Electives.objects.filter (major=userMajor)
            pos = Pos.objects.get (id=str (request.POST.get ('pos')))
            for elective in userElectives:
                coursesTaken = request.POST.getlist (str (elective.id) + "elective")
                for course in coursesTaken:
                    c = Courses.objects.get (id=course)
                    pos.neededCourses.add (c)

            courses = []
            for course in pos.neededCourses.all ():
                prereqs = Prerequisite.objects.filter (courseFor=course)
                setattr (course, 'prereqs', prereqs)
                courses.append (course)

            checkCourses = []
            for course in courses:
                checkprereqs = []
                for prereq in course.prereqs:
                    if prereq.course.department.id == 261:
                        checkprereqs.append (prereq)
                if len (checkprereqs) != 0:
                    setattr (course, 'checkprereqs', checkprereqs)
                    checkCourses.append (course)

            if len (courses) != 0:
                return render (request, 'base/new_check_prereq.html', {
                    'courses': checkCourses,
                    'posId': pos.id,
                    'userMajorId': userMajor.id
                }, context)
            else:
                pos = Pos.objects.get (id=str (request.POST.get ('pos')))
                userMajor = Majors.objects.get (id=str (request.POST.get ('major')))
                prereqs = request.POST.getlist ('prereqs')
                for prereq in prereqs:
                    course = Courses.objects.get (acronym=prereq)
                    pos.takenCourses.add (course)
                stack = []
                neededCourses = []
                nc = pos.neededCourses.all ().order_by ('number')
                for course in nc:
                    setattr (course, 'weight', 0)
                    stack.append (course)
                    neededCourses.append (course)
                while len (stack) != 0:
                    course = stack.pop ()
                    prereqs = Prerequisite.objects.filter (courseFor=course)
                    for prereq in prereqs:
                        if prereq.course.department.id != 262:
                            found = False
                            if prereq.course not in stack:
                                if prereq.course not in pos.takenCourses.all ():
                                    if prereq.course not in pos.neededCourses.all ():
                                        substitutes = Substitutes.objects.filter (courseFor=course,
                                                                                  courseSubOf=prereq.course)
                                        for substitute in substitutes:
                                            if substitute.course in pos.takenCourses.all ():
                                                found = True
                                    else:
                                        found = True
                                else:
                                    found = True
                            else:
                                found = True
                                setattr (stack[stack.index (prereq.course)], 'weight', course.weight + 1)
                            if found == False:
                                setattr (prereq.course, 'weight', course.weight + 1)
                                stack.insert (0, prereq.course)
                                if prereq.course not in pos.neededCourses.all ():
                                    setattr (prereq.course, 'weight', course.weight + 1)
                                    neededCourses.append (prereq.course)
                                    pos.neededCourses.add (prereq.course)
                        else:
                            if str (prereq.course.number) == 'CLASS':
                                setattr (course, 'class', prereq.course.acronym)
                            elif str (prereq.course.number) == 'CREDITS':
                                setattr (course, 'credits', prereq.course.acronym)

                def reverse_weight(x, y):
                    return y.weight - x.weight

                neededCourses = sorted (neededCourses, cmp=reverse_weight)
                for course in neededCourses:
                    print (str (course) + ": " + str (course.weight))


        elif str (request.path_info) == '/newcheckprereq':
            # Add user inputted prereqs to takenCourses
            pos = Pos.objects.get (id=str (request.POST.get ('pos')))
            userMajor = Majors.objects.get (id=str (request.POST.get ('major')))
            prereqs = request.POST.getlist ('prereqs')
            for prereq in prereqs:
                course = Courses.objects.get (id=prereq)
                pos.takenCourses.add (course)

            # Deal with prereqs
            stack = []
            neededCourses = []
            nc = pos.neededCourses.all ().order_by ('number')
            for course in nc:
                setattr (course, 'weight', 0)
                stack.append (course)
                neededCourses.append (course)
            while len (stack) != 0:
                course = stack.pop ()
                prereqs = Prerequisite.objects.filter (courseFor=course)
                for prereq in prereqs:
                    if prereq.course.department.id != 262:
                        found = False
                        if prereq.course not in stack:
                            if prereq.course not in pos.takenCourses.all ():
                                if prereq.course not in pos.neededCourses.all ():
                                    substitutes = Substitutes.objects.filter (courseFor=course,
                                                                              courseSubOf=prereq.course)
                                    for substitute in substitutes:
                                        if substitute.course in pos.takenCourses.all ():
                                            found = True
                                else:
                                    found = True
                            else:
                                found = True
                        else:
                            found = True
                            setattr (stack[stack.index (prereq.course)], 'weight', course.weight + 1)

                        if found == False:
                            setattr (prereq.course, 'weight', course.weight + 1)
                            print ("For course " + str (course) + " adding preq " + str (prereq.course))
                            stack.insert (0, prereq.course)
                            if prereq.course not in pos.neededCourses.all ():
                                setattr (prereq.course, 'weight', course.weight + 1)
                                neededCourses.append (prereq.course)
                                pos.neededCourses.add (prereq.course)
                    else:
                        if str (prereq.course.number) == 'CLASS':
                            setattr (course, 'class', prereq.course.acronym)
                        elif str (prereq.course.number) == 'CREDITS':
                            setattr (course, 'credits', prereq.course.acronym)

            # Deal with schedule of courses

            # Order classes by weight, largest at top, smallest at bottom
            def weight(x):
                return x.weight

            # Find max weight and total credits
            maxWeight = max (neededCourses, key=weight).weight
            totalcredits = 0

            # parse through credits string and return appropriate value
            def parse_credits(credits):
                # Some credits are a string, ex: "1-2"
                try:
                    int (credits)
                    return int (credits)
                except:
                    credits = credits.replace (" ", "")
                    credits = credits.replace ("-", " ")
                    credits = credits.split ()
                    try:
                        int (credits[0])
                        return int (credits[0])
                    except:
                        return int (0)

            # Add extra weight for basic program
            basicprogram = BasicProgram.objects.get (major=userMajor)
            for course in neededCourses:
                if course in basicprogram.courses.all ():
                    setattr (course, 'weight', course.weight + 6)
                    totalcredits = totalcredits + parse_credits (course.numCredits)

            # Estimate number of semesters
            minSemesters = totalcredits / 18
            if maxWeight > minSemesters:
                totalSemesters = maxWeight
            else:
                totalSemesters = minSemesters

            # Create empty semesters
            global semesters
            semesters = []
            for step in range (totalSemesters):
                s = Semesters.objects.create (order=step)
                s.save ()
                semesters.append (s)

            # Order classes by weight, smallest at top, largest at bottom
            def weight(x, y):
                return x.weight - y.weight

            neededCourses = sorted (neededCourses, cmp=weight)

            # for course in neededCourses:
            #     print (str (course) + ": " + str (course.weight))

            # Find earliest semester a course can be placed
            def findLatestSem(prereqs, semesters):
                count = 0
                numToFind = len (prereqs)
                latestSem = 0
                for semester in semesters:
                    for course in semester.courses.all ():
                        if course in prereqs:
                            count += 1
                            latestSem = semester.order
                        if count == numToFind:
                            return latestSem
                if numToFind != 0:
                    return -1
                return latestSem

            global buffer
            buffer = []
            global flag
            flag = False
            global placed
            placed = []

            def checkBuffer():
                if len(buffer) != 0:
                    global flag
                    flag = True
                else:
                    global flag
                    flag = False

            def put(order, course):
                global placed
                global semesters
                if order >= len(semesters):
                    semester = Semesters.objects.create (order=(order))
                    semester.save ()
                    semesters.append (semester)
                    put (int(semester.order), course)
                else:
                    semester = semesters[order]
                    credits = parse_credits (course.numCredits)
                    if int (semester.numCredits) + credits <= 18:
                        setattr (course, 'sem', semester.order)
                        semester.courses.add (course)
                        semester.numCredits = int (semester.numCredits) + int(credits)
                        placed.append (course)
                        # print ("Course " + str (course) + " placed in semester order = " + str (semester.order))
                        checkBuffer ()
                        return semester.order
                    else:
                        if int(semester.order + 1) > int(len(semesters) - 1) :
                            semester = Semesters.objects.create (order=(semester.order + 1))
                            semester.save ()
                            semesters.append (semester)
                            put (int(semester.order), course)
                        else:
                            put (int(semester.order+1), course)


            while len (neededCourses) != 0 or len (buffer) != 0:
                if len (neededCourses) == 0:
                    flag = True
                if flag == True:
                    if len (buffer) != 0:
                        course = buffer.pop ()
                        flag = False
                else:
                    course = neededCourses.pop ()

                # Get prereqs and coreqs
                # print ("")
                # print ("Checking " + str (course))
                prereqs = list (Prerequisite.objects.filter (courseFor=course))
                coreqs = list (Corequisite.objects.filter (courseFor=course))

                prereqCourses = []
                for prereq in prereqs:
                    if prereq.course not in pos.takenCourses.all():
                        prereqCourses.append(prereq.course)

                coreqCourses = []
                for coreq in coreqs:
                    if coreq.course in pos.takenCourses.all():
                        coreqCourses.append(coreq.course)

                # Logic for first avaliable semester
                if len (prereqCourses) != 0:
                    semCount = findLatestSem (prereqCourses, semesters) + 1
                    if semCount == 0:
                        buffer.append (course)
                        continue
                    if len (coreqCourses) == 0:
                        put (semCount, course)
                    else:
                        for coreq in coreqCourses:
                            if coreq in placed:
                                if placed[placed.index (coreq)].sem >= semCount:
                                    put (placed[placed.index (coreq)].sem, course)
                                else:
                                    put (semCount, course)
                            else:
                                coreqPrereq = Prerequisite.objects.filter (courseFor=coreq)
                                temp = []
                                for prereq in coreqPrereq:
                                    temp.append(prereq.course)

                                if len (temp) != 0:
                                    coreqSem = findLatestSem (temp, semesters) + 1
                                    if coreqSem == 0:
                                        buffer.append (course)
                                        buffer.append (coreq)
                                        continue
                                else:
                                    coreqSem = 0
                                coreqSem = put (coreqSem, coreq)
                                if coreqSem > semCount:
                                    put (coreqSem, course)
                                else:
                                    put (semCount, course)
                else:
                    semCount = 0
                    if len (coreqCourses) == 0:
                        if course.acronym == 'S E 494':
                            c = Courses.objects.get(acronym='S E 491')
                            put(placed[placed.index(c)].sem, course)
                        else:
                            put (semCount, course)
                    else:
                        for coreq in coreqCourses:
                            if coreq in placed:
                                if placed[placed.index (coreq)].sem >= semCount:
                                    put (placed[placed.index (coreq)].sem, course)
                                else:
                                    put (semCount, course)
                            else:
                                coreqPrereq = Prerequisite.objects.filter (courseFor=coreq)
                                temp = []
                                for prereq in coreqPrereq:
                                    temp.append(prereq.course)

                                if len (temp) != 0:
                                    coreqSem = findLatestSem (temp, semesters) + 1
                                    if coreqSem == 0:
                                        buffer.append (course)
                                        buffer.append (coreq)
                                        continue
                                else:
                                    coreqSem = 0
                                coreqSem = put (coreqSem, coreq)
                                if coreqSem > semCount:
                                    put (coreqSem, course)
                                else:
                                    put (semCount, course)

            # for semester in semesters:
            #     print ("Semester " + str (semester.order) + " " + str (semester.numCredits) + " credits")
            #     for course in semester.courses.all ():
            #         print (course)
            for semester in semesters:
                pos.semesters.add(semester)

            posAll = Pos.objects.filter (user=request.user).order_by ('-id')

            return render(request, 'base/view.html', {
                'pos': posAll,

            })
        elif str (request.path_info) == '/view':
            pos = Pos.objects.filter (user=request.user).order_by ('-id')
            display = Pos.objects.filter (user=request.user).order_by ('-id')[0].id
            if request.method == 'POST':
                toprint = request.POST.get ("submit", "0")
                display = request.POST.get ("generated", "0")
                if request.POST.get ("submit", "0") == 'deletePOS':
                    posDel = Pos.objects.get (id=display)
                    posDel.delete ()
                    toprint = request.POST.get ("submit", "0")
                    display = Pos.objects.filter (user=request.user).order_by ('-id')[0].id
                    return render (request, 'base/view.html', {
                        'pos': pos,
                    })

            return render (request, 'base/view.html', {
                'pos': pos,
            })

    return render (request, 'base/new.html', {
        'majors': majors,
        'electives': electives,
    })


def pos_view(request):
    pos = Pos.objects.filter (user=request.user).order_by ('-id')
    display = Pos.objects.filter (user=request.user).order_by ('-id')[0].id
    if request.method == 'POST':
        toprint = request.POST.get ("submit", "0")
        display = request.POST.get ("generated", "0")
        if request.POST.get ("submit", "0") == 'deletePOS':
            posDel = Pos.objects.get (id=display)
            posDel.delete ()
            toprint = request.POST.get ("submit", "0")
            display = Pos.objects.filter (user=request.user).order_by ('-id')[0].id
            return render (request, 'base/view.html', {
                'pos': pos,
            })

    return render (request, 'base/view.html', {
        'pos': pos,
    })


def index(request):
    return render (request, 'base/index.html')


# @author of function: Jens Petersen
def user_edit(request):
    user = request.user
    user_form = None
    context = RequestContext (request)
    print (vars (request))

    if request.method == 'POST':
        user_form = UserEditForm (request.POST, instance=request.user)

        if user_form.is_valid ():
            user = user_form.save ()
            return render (request, 'base/manage.html', {}, context)
        else:
            print (user_form.errors)

    else:
        user_form = UserForm (request.POST, instance=request.user)
        user_form.first_name = "user.first_name"

    return render (request, 'base/user_edit.html', {'user_form': user_form})


def user_password_edit(request):
    user = request.user
    user_form = None
    context = RequestContext (request)
    if request.method == 'POST':
        user_form = ChangePasswordForm (request.POST, instance=request.user)
        if user_form.is_valid ():
            cur = "before POST check"
            if request.user.check_password (request.POST['old_password']):
                cur = "Current and retyped old password match"
                print (cur)
                if request.POST['new_password_1'] == request.POST['new_password_2']:
                    print (request.user.check_password (request.POST['old_password']) == request.POST['new_password_1'])
                    if request.user.check_password (request.POST['new_password_1']):
                        cur = "problem: old password and new password match"
                        print (cur)
                        return render (request, 'base/user_password_edit.html', {'user_form': user_form})
                    else:
                        cur = "old password and new password don't match!! :)"
                        print (cur)
                        user.set_password (request.POST['new_password_1'])
                        user = user_form.save ()
                        user = authenticate (username=request.POST.get ('username'),
                                             password=request.POST.get ('password'))
                        return render (request, 'base/manage.html', {}, context)
                else:
                    cur = "problem: new_password_1 and new_password_2 don't match"
                    print (cur)
                    return render (request, 'base/user_password_edit.html', {'user_form': user_form})

            else:
                cur = "problem: Current and retyped old password don't match"
                print (cur)
                return render (request, 'base/user_password_edit.html', {'user_form': user_form})

        else:
            cur = "request not POST"
            print (cur)
            return render (request, 'base/manage.html', {}, context)
            print (user_form.errors)

    else:
        user_form = ChangePasswordForm (request.POST, instance=request.user)
        user_form.first_name = "user.first_name"
    return render (request, 'base/user_password_edit.html', {'user_form': user_form})


# Search view to be used with Haystack search
class SearchView (TemplateView):
    template_name = 'mysearch/search.html'


search_view = SearchView.as_view ()
