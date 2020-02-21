from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    skill = models.CharField(max_length = 100)   
    description = models.TextField()
    spaces = models.IntegerField()
    title = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100) 
    customer = models.ForeignKey(User, models.SET_NULL, blank = True, null = True) # foreign key user THIS WILL BE DELETED BECAUSE SESSION FK GOES IN USER

    def __str__(self):
        return self.title 