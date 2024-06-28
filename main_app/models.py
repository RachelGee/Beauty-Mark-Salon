from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STYLISTS = (
    ('A', 'Annabelle'),
    ('C', 'Corey'),
    ('D', 'Devlin'),
    ('G', 'Giang'),
    ('S', 'Scott'),
)

# Create your models here.
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    cost = models.IntegerField(0)
    stylists = models.CharField(
        max_length=1,
        choices=STYLISTS,
        default=STYLISTS[0][0]
    )

    parent_service = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.get_stylists_display()} on {self.date}"

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.id})
        


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
