from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def terms(request):
    return render(request, 'home/terms.html')

def privacy(request):
    return render(request, 'home/privacy.html')