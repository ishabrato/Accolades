from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("I am home")

def about(request):
    return HttpResponse("I am about page")