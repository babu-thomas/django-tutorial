from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Welcome to Polls app!</h1>')


def detail(request, question_id):
    return HttpResponse('Question #%s' % question_id)


def results(request, question_id):
    return HttpResponse('Results for question #%s' % question_id)


def vote(request, question_id):
    return HttpResponse('Voting page for question#%s' % question_id)
