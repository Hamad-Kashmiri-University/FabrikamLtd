from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm import usercreationform
from .models import *

class BookingForm(forms.ModelForm):
    #times = IndividualSession.objects.values_list('datetime', flat = True)
    #available = forms.ModelChoiceField(queryset=times)

    class Meta:
        model = Booking
        fields = ['individualsession', 'additionalrequirements'] 

    individualsession = forms.ModelChoiceField(queryset=IndividualSession.objects.filter(session__pk=1))
