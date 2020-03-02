from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    skill = models.CharField(max_length = 100)   
    description = models.TextField()
    spaces = models.IntegerField()
    title = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100) 
    teacher = models.ForeignKey(User, models.SET_NULL, blank = True, null = True) # foreign key user THIS WILL BE DELETED BECAUSE SESSION FK GOES IN USER

    def __str__(self):
        return self.title 
    
class IndividualSession(models.Model):
    datetime = models.DateTimeField()
    session = models.ForeignKey(Session, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.session.title} Session'

class Booking(models.Model):
    individualsession = models.ForeignKey(IndividualSession, on_delete = models.CASCADE)
    additionalrequirements = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relationship with a user

