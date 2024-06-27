from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    cost = models.IntegerField()

    def __str__(self):
        return self.type

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
