from django.shortcuts import render
from django.http import HttpResponse
#home handles traffic from homepage of reviews and takes req

def home(request):
    return HttpResponse('<h1>Bookings<h1>')
