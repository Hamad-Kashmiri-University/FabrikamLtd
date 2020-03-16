from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking, Session, IndividualSession
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from datetime import *

#handles traffic takes req and returns httpresponse
#calsses is dummy dict for testing

tmrtime = datetime.now() + timedelta(hours = 24)#used in filtering avail

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
    paginate_by = 4         #pagination 


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    #fields = ['individualsession', 'additionalrequirements']
    template_name = 'Bookings/details.html'
 
    def form_valid(self, form):
        print(self.request.user.username)
        form.instance.user = self.request.user
        #BookingForm.instance.individualsession = self.request.individualsession
        #booking.user = User.objects.get(user=self.request.user)
        return super().form_valid(form)

@login_required
def BookingView(request, pk):
    if request.method == "POST":
        form =  BookingForm(request.POST)
        form.fields["individualsession"].queryset = IndividualSession.objects.all().filter(session__pk=pk, isbooked=False, sessiontime__gt = tmrtime) # filter by session instance pk and if not booked and if time within 24 hours
        form.instance.user = request.user    #set logged user to user   
        if form.is_valid():
            bookcount = Booking.objects.all().filter(individualsession__pk=form.instance.individualsession.pk).count()#perform full check here count bookings and compare to session spaces relational comparison
            if bookcount + 1 < form.instance.individualsession.session.spaces:   
                print(bookcount)
                print(form.instance.individualsession.session.spaces)#perform full check here
                form.save()
                messages.success(request, f'Booking Successful')
                return redirect('profile')
            elif bookcount + 1 == form.instance.individualsession.session.spaces:   # the instance will be 1 behind as it is not saved yet
                print(bookcount)
                print(form.instance.individualsession.session.spaces)#perform full check here
                fullsession = IndividualSession.objects.all().filter(pk=form.instance.individualsession.pk).get()
                fullsession.isbooked = True # set to booked session so it wont show up after
                fullsession.save()  
                print(fullsession)
                form.save()
                messages.success(request, f'Booking Successful, You have the last spot for this session')
                return redirect('profile')

    else:
        form = BookingForm()
        form.fields["individualsession"].queryset = IndividualSession.objects.all().filter(session__pk=pk, isbooked=False,  sessiontime__gt = tmrtime)#DYNAMIC FILTERING

    return render(request, "Bookings/details.html", {'form': form})
    

  