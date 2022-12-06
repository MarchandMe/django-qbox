from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse
from .models import Question

def indexpage(request):
    QAs = Question.objects.filter(status = 1)
    context = {
        'questions' : QAs,
    }
    return render(request, 'QuestionList.html', context)

def addquestionpage(request):
    return render(request, 'AddQuestion.html')

def addingquestionpage(request): #this is for when the submit button is pressed
  Q = request.POST['question']
  newq = Question(question = Q)
  newq.save()
  return HttpResponseRedirect(reverse('home'))