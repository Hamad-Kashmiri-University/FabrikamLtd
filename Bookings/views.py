from django.shortcuts import render
from django.http import HttpResponse
#handles traffic takes req and returns httpresponse
#calsses is dummy dict for testing
classes = [
    {
        'title': 'Microsoft Word',
        'skill': 'easy',
        'date': '10th julember',
        'spaces': '20'
    },

        {
        'title': 'Microsoft Excel',
        'skill': 'easy',
        'date': '12th julember',
        'spaces': '25',
    },
]

def home(request):
    context = {                 # dict with key classes and above list of dicts paired
        'classes': classes
    }
    return render(request, 'Bookings/home.html', context) # context is the above defined passed to the page

def detail(request):
    return render(request, 'Bookings/details.html', {'title': 'Booking'})