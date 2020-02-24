from django.shortcuts import render
from django.http import HttpResponse
from .models import Session 
#handles traffic takes req and returns httpresponse
#calsses is dummy dict for testing


def home(request):
    context = {                 # dict with key classes and above list of dicts paired
        'session': Session.objects.all(),  # passing data from Session model in models.py from this directory called in the imports
        'pagetitle': "placeholder"
    }
    return render(request, 'Bookings/home.html', context) # context is the above defined passed to the page

def detail(request):
    return render(request, 'Bookings/details.html', {'pagetitle': 'Booking'})