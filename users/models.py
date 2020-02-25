from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relationship with a user
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
#add more stuff in the profile here

    def __str__(self):
        return f'{self.user.username} Profile' # string to pring when referencing a user profile
