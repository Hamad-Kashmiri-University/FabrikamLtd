from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Session(models.Model):
    skill = models.CharField(max_length = 100)   
    description = models.TextField()
    spaces = models.IntegerField()
    title = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100) 
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default = 2) # foreign key user THIS WILL BE DELETED BECAUSE SESSION FK GOES IN USER

    def __str__(self):
        return self.title 
       

    
class IndividualSession(models.Model):
    datetime = models.DateTimeField()
    session = models.ForeignKey(Session, on_delete = models.CASCADE)
    isbooked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.session.title} at {self.datetime}'

class Booking(models.Model):
    individualsession = models.ForeignKey(IndividualSession, on_delete = models.CASCADE, null = True)
    additionalrequirements = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) # one to one relationship with a user

    def __str__(self):
        return f'{self.user} Booking'
            
            
    def get_absolute_url(self):
        return reverse('profile')