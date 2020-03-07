from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Session, IndividualSession, Booking 
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
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
        print(pk)
        form =  BookingForm(request.POST)
        form.fields["individualsession"].queryset = IndividualSession.objects.all().filter(session__pk=pk)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f'Booking Successful')
            return redirect('profile')
        
    else:
        form = BookingForm()
        form.fields["individualsession"].queryset = IndividualSession.objects.all().filter(session__pk=pk)#DYNAMIC FILTERING

    return render(request, "Bookings/details.html", {'form': form})
    

  