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

SERVICE = [
    ('B', 'Blowout'),
    ('WCS', 'Womens Cut & Style'),
    ('WMC', 'Womens Master Cut & Style'),
    ('MCW', 'Mens Wash & Scissor Cut'),
    ('LMC', 'Lengthy Master Color'),
    ('BMC', 'Buzz Master Color'),
    ('F', 'Fix Your Face'),
    ('FF', 'Face First'),
]


# Create your models here.
# SERVICES
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    cost = models.IntegerField(0)
    

    parent_service = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.get_stylists_display()}"

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.id})
        

# APPOINTMENTS
class Appointment(models.Model):
    date = models.DateField('Booking date')
    service = models.CharField(
        max_length=3,
        choices=SERVICE,
        default=SERVICE[0][0]
    )
    stylists = models.CharField(
        max_length=1,
        choices=STYLISTS,
        default=STYLISTS[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']