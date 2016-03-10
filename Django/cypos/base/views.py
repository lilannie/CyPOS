from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<p>In index view</p>')


def user_detail(request, id):
    return HttpResponse('<p>In user_detail view with id {0}</p>'.format(id))