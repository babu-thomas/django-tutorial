from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    return HttpResponse('Results for question #%s' % question_id)


def vote(request, question_id):
    return HttpResponse('Voting page for question#%s' % question_id)
