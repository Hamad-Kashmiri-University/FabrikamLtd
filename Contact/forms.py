#Code by Finlay Campbell
from django import forms
from Contact.models import suppTicket

class suppTicketForm(forms.ModelForm):
    name = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    message = forms.CharField( widget=forms.Textarea(attrs={'class': "form-control"}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = suppTicket
        fields = ['name', 'email', 'subject', 'message',]