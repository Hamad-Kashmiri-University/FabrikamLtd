from django import forms
from Contact.models import suppTicket

class suppTicketForm(forms.ModelForm):
    class Meta:
        model = suppTicket
        fields = ['name', 'email', 'subject', 'message',]