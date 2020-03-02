from django.shortcuts import render
from django.http import HttpResponse
from .models import Session, IndividualSession, Booking 
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BookingForm
#handles traffic takes req and returns httpresponse
#calsses is dummy dict for testing


def home(request):
    context = {                 # dict with key classes and above list of dicts paired
        'session': Session.objects.all(),  # passing data from Session model in models.py from this directory called in the imports
        'pagetitle': "placeholder"
    }
    return render(request, 'Bookings/home.html', context) # context is the above defined passed to the page

class SessionListView(ListView):
    model = Session
    template_name='Bookings/home.html' # what the browser looks for in class views
    context_object_name = 'session'
    ordering = ['-spaces'] # orders by descending spaces

'''class SessionDetailView(DetailView):
    model = Session
    template_name='Bookings/details.html'
    context_object_name = 'session


   class SessionCreateView(CreateView):
    model = Session
    fields = ['skill', 'description', 'spaces', 'title', 'teacher']'''

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'Bookings/details.html'
    

    def form_valid(self, form):
        booking = form.save(commit = False)
        booking.user = User.objects.get(user=self.request.user)
        booking.save()  
        f.save()
        return HttpResponseRedirect(self.get_success_url())



  

  