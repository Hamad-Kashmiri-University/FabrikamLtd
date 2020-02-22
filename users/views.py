from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)#creates a form with the POST data so if not valid some data still in the form
        if form.is_valid():
            form.save() # auto hashes password for security
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}') # pop up message for user
            return redirect("Bookings")
    else:
        form = UserRegisterForm()
    #checks if post request try to validate the form data, otherwise instantiate empty form
    return render(request, 'users/register.html', {'form': form})
    

