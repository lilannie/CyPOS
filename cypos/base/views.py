from django.shortcuts import render
from .forms import UserForm
from .models import Courses, Majors, Pos, Electives, Departments, Colleges
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
        courses = Courses.objects.get(id=id).order_by('number')
    except Courses.DoesNotExist:
        courses = []
    return render(request, 'base/course_department.html', {
        'courses': courses
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
    majors = Majors.objects.all()
    electives = Electives.objects.all()

    if request.method == 'POST':
        print(request.POST.get('major'))
        userMajor = Majors.objects.get(id=str(request.POST.get('major')))
        pos = Pos.objects.create(user=request.user, major=userMajor)
        pos.save()

        for reqCourse in userMajor.reqCourses.all():
            if str(request.POST.get(str(reqCourse.id))) != 'None':
                course = Courses.objects.get(acronym=request.POST.get(str(reqCourse.id)))
                pos.takenCourses.add(course)
            else:
                course = Courses.objects.get(id=reqCourse.id)
                pos.neededCourses.add(course)
        # print(request.POST.get(str(number)))

        # print(pos.takenCourses.all())
        return render(request, 'base/view.html', {}, context)

    return render(request, 'base/new.html', {
        'majors': majors,
        'electives': electives,
    })


def user_detail(request, id):
    return render(request, 'user/user_detail.html', {
        # 'user': user,
    })


def pos_view(request):
    try:
        pos = Pos.objects.filter(user=request.user).order_by('-id')[0]
    except:
        pos = []
    return render(request, 'base/view.html', {
        'pos': pos
    })


def index(request):
    return render(request, 'base/index.html')


# @author of function: Jens Petersen
def user_edit(request):
    user = request.user
    user_form = None
    context = RequestContext(request)
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return render(request, 'base/user_edit.html', {}, context)
        else:
            print(user_form.errors)
    # What're you do when it's not a post? When you just wanna display the form?
    else:
        user = request.user
        user_form = UserForm(request.POST, instance=request.user)
       # user_form.save()
    return render(request, 'base/user_edit.html', {'user_form': user_form})


class UserEditForm():
    def get(request):
        form = forms.UserEditForm(instance=team)
        context['form'] = form
        return self.render_to_response(context)
    # Origin: iseage signup github repo
    #def post(self, request, context, *args, **kwargs):
    #     team = context['participant'].team
    #     form = base_forms.ModifyTeamForm(data=request.POST, instance=team)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Team successfully updated.')
    #         return redirect('manage-team')
    #     #If the form was invalid, get the old participant object back
    #     context['participant'] = request.user.participant
    #     return self.get(request, context, form=form)