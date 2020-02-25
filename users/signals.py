from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#create a profile everytime a user is created
@receiver(post_save, sender=User) #when a user is saved send postsave signal to be received by below func
def create_profile(sender, instance, created, **kwargs): #takes args that post save passes
    if created:
        Profile.objects.create(user=instance) # create a profile with the instance of the user that was sent here

#save profile when user is saved
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs): #kwargs accepts additional key word argyments
    instance.profile.save()