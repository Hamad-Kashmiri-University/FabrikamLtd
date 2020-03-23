from django.shortcuts import render
from django.shortcuts import redirect
from Contact.forms import suppTicketForm
from Contact.models import suppTicket

def contact(request):
    form = suppTicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("Home")
    else:
        return render(request, 'Contact/contact.html', {'form': form})

