from django.db import models

class suppTicket(models.Model):
    message = models.CharField(max_length=300)
    email = models.EmailField(max_length=150)
    name = models.CharField(max_length=50)
    supptype = models.CharField(max_length=300)

    def __str__(self):
        return self.title
