from django.shortcuts import render
from django.http import HttpResponse
#handles traffic takes req and returns httpresponse

def home(request):
    return HttpResponse('<h1>Bookings<h1>')

def detail(request):
    return HttpResponse('<h1>booking detail<h1>')