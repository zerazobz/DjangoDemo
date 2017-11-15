from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello world this is the index for the polls.")

def detail(request, question_id):
    return HttpResponse("You're looking at the question $s."%question_id)

def results(request, question_id):
    response = "You're looking at the results of the question %s"
    return HttpResponse(response%question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s"%question_id)