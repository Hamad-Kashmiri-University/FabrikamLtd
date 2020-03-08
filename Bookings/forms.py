from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm import usercreationform
from .models import *

class BookingForm(forms.ModelForm):
    #times = IndividualSession.objects.values_list('datetime', flat = True)
    #available = forms.ModelChoiceField(queryset=times)
    individualsession = forms.ModelChoiceField(queryset=IndividualSession.objects.all(), label = "Select Timeslot")
    additionalrequirements = forms.CharField(label = "Special/Dietary Requirements (N/A if none)")
    class Meta:
        model = Booking
        fields = ['individualsession', 'additionalrequirements'] 
        

