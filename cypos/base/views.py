from django.shortcuts import render
from django.http import Http404
# from django.http import HttpResponse

from .models import TestUsers
from .models import TestCourses


def courses_view(request):
    courses = TestCourses.objects.all()
    return render(request, 'base/courses.html', {
        'courses': courses,
    })


def help(request):
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
    try:
        user = TestUsers.objects.get(id=id)
    except TestUsers.DoesNotExist:
        raise Http404('This user does not exist')
    return render(request, 'user/user_detail.html', {
        'user': user,
    })


def pos_view(request):
    return render(request, 'base/view.html')


def index(request):
    return render(request, 'base/index.html')
