from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CreateSessionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from Bookings.models import Booking, Session, IndividualSession 
from .models import Profile
from datetime import datetime, timedelta
from django.http import JsonResponse 
import json # for js we need json format

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

def get_data(request, *args, **kwargs):
    labels1 = []    
    data1vals = [] #contains values
    data1 = []   #contains the count
    chartlabels = Session.objects.all()
    chartdata = Booking.objects.all().filter(user = request.user).order_by("individualsession__sessiontime")  # get queryset for chart
    for session in chartlabels:
        labels1.append(session.title)   
    for each in chartdata:
        data1vals.append(each.individualsession.session.id)
    data1vals = set(data1vals) # get unique items
    data1vals = list(data1vals)
    for val in range(len(data1vals)):
        print(val)
        data1.append(0)
    for booking in chartdata:
        for index in range(len(data1vals)):
            if booking.individualsession.session.id == data1vals[index]:
                data1[index] += 1
    #make vals list with id for ecah session a person has booked
    #make a data list with 0 for each session booked
    # compare bookng session id with id in list and increment by 1 to get total for each item
    data = {
        "labels": labels1,
        "data": data1
    }
    return JsonResponse(data)
    #we get jsonresponse not htmlresp so we can get json data to use in any page

@login_required  #login decorator user must be logged in to view this page , this is the reason we dont pass user data as a user must be logged in 
def profile(request):
    labels1 = []
    data1vals = [] #contains values
    data1 = []   #contains the count
    chartlabels = Session.objects.all()
    chartdata = Booking.objects.all().filter(user = request.user).order_by("individualsession__sessiontime")  # get queryset for chart
    for session in chartlabels:
        labels1.append(session.title)   
    for each in chartdata:
        data1vals.append(each.individualsession.session.id)
    data1vals = set(data1vals) # get unique items
    data1vals = list(data1vals)
    for val in range(len(data1vals)):
        print(val)
        data1.append(0)
    for booking in chartdata:
        for index in range(len(data1vals)):
            if booking.individualsession.session.id == data1vals[index]:
                data1[index] += 1
    data = json.dumps(data1) # return back into a list 
    labels = json.dumps(labels1)
    print(data1vals)
    print(data1)
    print(labels1)
    print(labels, data)
    #for loop to get chart vals
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
        'bookings': Booking.objects.all().filter(user = request.user, individualsession__sessiontime__gt = tmrtime) #24 hours future
        # dynamic filtering above using foreign key attrs 
     }
    return render(request, 'users/profile.html', context)


#same as user profile in terms of form however different stuff overall page
@login_required
def teacherprofile(request):
    get_data = get_data()
    if not request.user.profile.is_teacher:
        return redirect("profile")
    u_form = UserUpdateForm(instance=request.user) # pass in current users info to the forms
    p_form = ProfileUpdateForm(instance=request.user.profile)
    newsession_form = CreateSessionForm()
    sessionlist = IndividualSession.objects.all().filter(session__teacher = request.user).order_by('sessiontime', 'id')
    bookinglist = Booking.objects.all().filter(individualsession__session__teacher = request.user).order_by('individualsession')
    print(bookinglist)
    print(sessionlist)
    if request.method == "POST": 
        if 'profileupdateform' in request.POST:
            u_form = UserUpdateForm(request.POST, instance=request.user) # pass in current users info to the forms
            p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES,
                                    instance=request.user.profile)
            
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Account Updated Successfully') # pop up message for user
                return redirect("profile")
       
        # elif statement to separate post reqs below handles delete functionality
        elif 'pk' in request.POST:
            print(request.POST['pk'])
            print(Booking.objects.all().filter(pk=1))
            Booking.objects.all().filter(pk=request.POST['pk']).delete()
            return redirect('profile')
        
        elif 'createsession' in request.POST:
            newsession_form = CreateSessionForm(request.POST)
            if newsession_form.is_valid():
                newsession_form.save()
                messages.success(request, f'Session Created Successfully')
                return redirect('profile')
   
    else: 
        u_form = UserUpdateForm(instance=request.user) # pass in current users info to the forms
        p_form = ProfileUpdateForm(instance=request.user.profile)
        newsession_form = CreateSessionForm()
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'newsession_form': newsession_form, 
        'pagetitle': 'Teacher',
        'booking': bookinglist,
        'session': sessionlist
        

    }
    return render(request, 'users/teacherprofile.html', context)

