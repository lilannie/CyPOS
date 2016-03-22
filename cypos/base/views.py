from django.shortcuts import render
# from django.http import Http404
# from django.http import HttpResponse
from .forms import UserForm
from .models import TestCourses
from django.template import RequestContext


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

            # Update our variable to tell the template registration was successful.
            registered = True

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


def courses_view(request):
    courses = TestCourses.objects.all()
    return render(request, 'base/courses.html', {
        'courses': courses,
    })


def user_help(request):
    return render(request, 'base/help.html')


def pos_history(request):
    return render(request, 'base/history.html')


def home(request):
    return render(request, 'base/home.html')


def user_manage(request):
    return render(request, 'base/manage.html')


def pos_new(request):
    return render(request, 'base/new.html')


def user_detail(request, id):
    return render(request, 'user/user_detail.html', {
        # 'user': user,
    })


def pos_view(request):
    return render(request, 'base/view.html')


def index(request):
    return render(request, 'base/index.html')
