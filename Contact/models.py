#Code by Finlay Campbell
from django.db import models

class suppTicket(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.title
