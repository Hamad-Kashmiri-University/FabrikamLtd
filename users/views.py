from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from Bookings.models import Booking, Session, IndividualSession 
from .models import Profile
from datetime import datetime, timedelta

tmrtime = datetime.now() + timedelta(hours = 24)#used in filtering bookings for profile
def CustomLoginView(LoginView):
    if request.method == "POST":
        form = authentication_form(request.POST, instance=request.user)
        if form.is_valid and request.user.profile.is_teacher:
            form.save()
    return render(request, 'users/teacherprofile.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)#creates a form with the POST data so if not valid some data still in the form
        if form.is_valid():
            form.save() # auto hashes password for security
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, you can now login!') # pop up message for user
            return redirect("login")
    else:
        form = UserRegisterForm()
    #checks if post request try to validate the form data, otherwise instantiate empty form
    return render(request, 'users/register.html', {'form': form})

@login_required  #login decorator user must be logged in to view this page , this is the reason we dont pass user data as a user must be logged in 
def profile(request):
    if request.user.profile.is_teacher:
        return redirect("teacherprofile")
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user) # pass in current users info to the forms
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated Successfully') # pop up message for user
            return redirect("profile")
    
    else: 
        u_form = UserUpdateForm(instance=request.user) # pass in current users info to the forms
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'bookings': Booking.objects.all().filter(user = request.user, individualsession__sessiontime__gt = tmrtime)
        # dynamic filtering above using foreign key attrs 
     }
    return render(request, 'users/profile.html', context)

#same as user profile in terms of form however different stuff overall page
@login_required
def teacherprofile(request):
    sessionlist = IndividualSession.objects.all().filter(session__teacher = request.user).order_by('id')
    bookinglist = Booking.objects.all().filter(individualsession__session__teacher = request.user).order_by('individualsession')
    print(bookinglist)
    print(sessionlist)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user) # pass in current users info to the forms
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated Successfully') # pop up message for user
            return redirect("profile")
    
    else: 
        u_form = UserUpdateForm(instance=request.user) # pass in current users info to the forms
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'pagetitle': 'Teacher',
        'booking': bookinglist,
        'session': sessionlist
        

    }
    return render(request, 'users/teacherprofile.html', context)



