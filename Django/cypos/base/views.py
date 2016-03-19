from django.shortcuts import render
from django.http import Http404
# from django.http import HttpResponse

from .models import TestUsers
from .models import TestCourses


def index(request):
    return render(request, 'base/index.html')


def user_detail(request, id):
    try:
        user = TestUsers.objects.get(id=id)
    except TestUsers.DoesNotExist:
        raise Http404('This user does not exist')
    return render(request, 'user/user_detail.html', {
        'user': user,
    })


def courses_view(request):
    courses = TestCourses.objects.all()
    return render(request, 'base/courses.html', {
        'courses': courses,
    })