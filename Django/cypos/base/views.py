from django.shortcuts import render
from django.http import Http404
# from django.http import HttpResponse

from base.models import Users
from base.models import Courses


def index(request):
    return render(request, 'base/index.html')


def user_detail(request, id):
    try:
        user = Users.objects.get(id=id)
    except Users.DoesNotExist:
        raise Http404('This user does not exist')
    return render(request, 'user/user_detail.html', {
        'user': user,
    })


def courses_view(request):
    courses = Courses.objects.all()
    return render(request, 'base/courses.html', {
        'courses': courses,
    })