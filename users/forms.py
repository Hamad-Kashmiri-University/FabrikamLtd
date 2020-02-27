from django import forms
from django.contrib.auth.models import User  # import user
from django.contrib.auth.forms import UserCreationForm #import usercreationform
from .models import Profile


class UserRegisterForm(UserCreationForm): # add email field
    email = forms.EmailField()

    class Meta:
        model = User # user model
        fields = ['username', 'email', 'password1', 'password2'] # order we save form data to db

        #pass now userregisterform to db with updated fields

class UserUpdateForm(forms.ModelForm): 
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']