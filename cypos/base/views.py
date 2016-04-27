from django.shortcuts import render
from .forms import UserForm, UserEditForm, ChangePasswordForm
from .models import Courses, Majors, Pos, Electives, Departments, Colleges, PosElective
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.auth.models import User


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            login(request, user)
            # Update our variable to tell the template registration was successful.

            return render(request, 'base/home.html', {}, context)

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request, 'base/register.html', {'user_form': user_form, 'registered': registered}, context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return render(request, 'base/home.html', {}, context)
            else:
                # An inactive account was used - no logging in!
                return render(request, 'base/index.html', {}, context)
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'base/index.html', {}, context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'base/index.html', {}, context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return render(request, 'base/index.html', {})


def courses_view(request):
    departments = Departments.objects.all()
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
            ag.append(department)
        elif department.college_id == 2:
            bus.append(department)
        elif department.college_id == 3:
            des.append(department)
        elif department.college_id == 4:
            eng.append(department)
        elif department.college_id == 5:
            grad.append(department)
        elif department.college_id == 6:
            hs.append(department)
        elif department.college_id == 7:
            las.append(department)
        elif department.college_id == 8:
            vet.append(department)

    return render(request, 'base/courses.html', {
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
        courses = Courses.objects.filter(department_id=id).order_by('number')
        department = Departments.objects.get(id=id)
    except Courses.DoesNotExist:
        courses = []
        department = []
    return render(request, 'base/course_department.html', {
        'courses': courses,
        'department': department,
    })


def user_help(request):
    return render(request, 'base/help.html')


def pos_history(request):
    return render(request, 'base/history.html')


def home(request):
    return render(request, 'base/home.html')


def user_manage(request):
    user = request.user
    try:
        pos = Pos.objects.filter(user=request.user).order_by('-id')[0]
        takenCourses = pos.takenCourses.all()
    except:
        pos = []
        takenCourses = []
    return render(request, 'base/manage.html', {
        'user': user,
        'pos': pos,
        'takenCourses': takenCourses
    })


def pos_new(request):
    context = RequestContext(request)
    # majors = Majors.objects.all()
    se = Majors.objects.get(name="Software Engineering")
    cpre = Majors.objects.get(name="Computer Engineering")
    cs = Majors.objects.get(name="Computer Science")
    majors = {se, cpre, cs}
    electives = Electives.objects.all()

    if request.method == 'POST':
        print(request.POST.get('major'))
        userMajor = Majors.objects.get(id=str(request.POST.get('major')))
        pos = Pos.objects.create(user=request.user, major=userMajor)
        pos.save()

        electiveCourses = []
        electivesNeeded = []

        userElectives = Electives.objects.filter(major=userMajor)
        for elective in userElectives:
            posElective = PosElective.objects.create(pos=pos, elective=elective)
            creditsTaken = 0
            for course in elective.courses:
                if str(request.POST.get(str(course.id))) != 'None':
                    course = Courses.objects.get(acronym=request.POST.get(str(course.id)))
                    posElective.takenCourses.add(course)
                    creditsTaken = creditsTaken + course.numCredits
                    electiveCourses.append(course)

            if(elective.creditNum - creditsTaken < 0):
                posElective.creditsNeeded = 0
            else:
                posElective.creditsNeeded = elective.creditNum - creditsTaken
                electivesNeeded.append(posElective)

            posElective.save()

        for reqCourse in userMajor.reqCourses.all():
            if str(request.POST.get(str(reqCourse.id))) != 'None':
                course = Courses.objects.get(acronym=request.POST.get(str(reqCourse.id)))
                pos.takenCourses.add(course)
            else:
                course = Courses.objects.get(id=reqCourse.id)
                pos.neededCourses.add(course)

        for courses in electiveCourses:
            pos.takenCourses.add(course)

        coursesNeeded = pos.neededCourses.all
        pos = Pos.objects.filter(user=request.user).order_by('-id')
        return render(request, 'base/view.html', {
            'pos': pos,
            'coursesNeeded': coursesNeeded,
            'electivesNeeded': electivesNeeded,
        }, context)

    return render(request, 'base/new.html', {
        'majors': majors,
        'electives': electives,
    })


def user_detail(request, id):
    return render(request, 'user/user_detail.html', {
        # 'user': user,
    })


def pos_view(request):
    pos = Pos.objects.filter(user=request.user).order_by('-id')
    neededCourses = []
    display = Pos.objects.filter(user=request.user).order_by('-id')[0].id
    temp = Pos.objects.filter(user=request.user).order_by('-id')[0]
    print vars(temp.neededCourses.all)
    #print vars(Pos.objects.filter(user=request.user).order_by('-id')[0])
    if request.method == 'POST':
        # print(request.POST)
        # print vars(request)
        toprint = request.POST.get("submit", "0")
        display = request.POST.get("generated", "0")
        # print(toprint)
        # print(display)
        if request.POST.get("submit", "0") == 'posSwitch':  
            return render(request, 'base/view.html', {
                'pos': pos,
                'neededCourses': neededCourses,
                'display': display
            })
        if request.POST.get("submit", "0") == 'deletePOS':         
            posDel = Pos.objects.get(id=display)
            # print(posDel.id)
            # print vars(posDel)
            posDel.delete()
            toprint = request.POST.get("submit", "0")
            display = Pos.objects.filter(user=request.user).order_by('-id')[0].id
            return render(request, 'base/view.html', {
                'pos': pos,
                'neededCourses': neededCourses,
                'display': display
            })

        # pos = Pos.objects.filter(user=request.user).order_by('-id')
        # neededCourses = []
        # display = request.POST.get("display", "0")            
        # print(display)
        # return render(request, 'base/view.html', {
        #     'pos': pos,
        #     'neededCourses': neededCourses,
        #     'display': display
        # })

    # print(display)
    return render(request, 'base/view.html', {
        'pos': pos,
        'neededCourses': neededCourses,
        'display': display
    })


def index(request):
    return render(request, 'base/index.html')


# @author of function: Jens Petersen
def user_edit(request):
    user = request.user
    user_form = None
    context = RequestContext(request)
    print vars(request)
    
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        
        
        if user_form.is_valid():
            user = user_form.save()
            return render(request, 'base/manage.html', {}, context)
        else:
           print (user_form.errors)
    
    else:
        user_form = UserForm(request.POST, instance=request.user)
        user_form.first_name = "user.first_name"
       
    return render(request, 'base/user_edit.html', {'user_form': user_form})

def user_password_edit(request):
    user = request.user
    user_form = None
    context = RequestContext(request)
    if request.method == 'POST':
        #print vars(request)
        user_form = ChangePasswordForm(request.POST, instance=request.user)   
        # print(request.POST['old_password'])
        # print(request.POST['new_password_1'])
        # print(request.POST['new_password_2'])       
        if user_form.is_valid():
            #print vars(request)
            # print(request.user.check_password(request.POST['old_password']))
            # print(request.POST['old_password'])
            # print(request.POST['new_password_1'])
            # print(request.POST['new_password_2'])
            cur = "before POST check"
            if request.user.check_password(request.POST['old_password']):
                cur = "Current and retyped old password match"
                print(cur)
                if request.POST['new_password_1'] == request.POST['new_password_2']:
                    print(request.user.check_password(request.POST['old_password']) == request.POST['new_password_1'])
                    if request.user.check_password(request.POST['new_password_1']):
                        cur = "problem: old password and new password match"
                        print(cur)
                        return render(request, 'base/user_password_edit.html', {'user_form': user_form})
                    else:                   
                        cur = "old password and new password don't match!! :)"
                        print(cur)
                        user.set_password(request.POST['new_password_1'])
                        user = user_form.save()
                        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
                        return render(request, 'base/manage.html', {}, context) 
                else: 
                    cur = "problem: new_password_1 and new_password_2 don't match"
                    print(cur)
                    return render(request, 'base/user_password_edit.html', {'user_form': user_form})
                    
            else:
                cur = "problem: Current and retyped old password don't match"
                print(cur)
                return render(request, 'base/user_password_edit.html', {'user_form': user_form})
            
        else:
            cur = "request not POST"
            print(cur)
            return render(request, 'base/manage.html', {}, context)
            print (user_form.errors)
    
    else:
        user_form = ChangePasswordForm(request.POST, instance=request.user)
        user_form.first_name = "user.first_name"
        #print(user.first_name)
        #user_form = UserEditForm(request.POST, instance=request.user)
       # user_form.save()
    return render(request, 'base/user_password_edit.html', {'user_form': user_form})

# Search view to be used with Haystack search
class SearchView(TemplateView):
    template_name = 'mysearch/search.html'
search_view = SearchView.as_view()