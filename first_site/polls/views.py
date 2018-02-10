from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse('Question #%s' % question_id)


def results(request, question_id):
    return HttpResponse('Results for question #%s' % question_id)


def vote(request, question_id):
    return HttpResponse('Voting page for question#%s' % question_id)
