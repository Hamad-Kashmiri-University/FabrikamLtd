from django import forms
from django.contrib.auth.models import User  # import user
from django.contrib.auth.forms import UserCreationForm #import usercreationform

class UserRegisterForm(UserCreationForm): # add email field
    email = forms.EmailField()

    class Meta:
        model = User # user model
        fields = ['username', 'email', 'password1', 'password2'] # order we save form data to db

        #pass now userregisterform to db with updated fields