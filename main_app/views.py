# main_app/views.py

from django.shortcuts import render, redirect
from .models import Service, Appointment
from django.contrib.auth.views import LoginView


# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# HOME
# def home(request):
#     return render(request, 'home.html', {'home': home})
class Home(LoginView):
    template_name = 'home.html'


# SERVICES
def service_index(request):
    return render(request, 'services/index.html', {'services': services})

def service_detail(request, service_id):
    service = Service.objects.get(id=service_id)
    return render(request, 'services/detail.html', {'service-detail': service})

class Service:
    def __init__(self, type, description, cost, image):
        self.type = type
        self.description = description
        self.cost = cost
        self.image = image
        

services = [
    Service('Blowout', '', 40, image='images/blowout.png'),
    Service('Womens Cut & Style', '', 60, image='images/womenscutstyle.png'),
    Service('Womens Master Cut & Style', '', 65, image='images/mastercutstyle.png'),
    Service('Mens Wash & Scissor Cut', '', 40, image='images/menswashcut.png'),
    Service('Lengthy Master Color', '', 200, image='images/lengthmastercolor.png'),
    Service('Buzz Master Color', '', 100, image='images/buzzmastercolor.png'),
    Service('Fix Your Face', 'Standard makeup', 60, image='images/fixyourface.png'),
    Service('Face First', 'Master makeup', 90, image='images/facefirst.png'),
]


# ABOUT
def about(request):
    # Send a simple HTML response
    return render(request, 'about.html')

# APPOINTMENTS
def appointments(request):
    return render(request, 'appointments.html')

# GALLERY
def gallery(request):
    return render(request, 'gallery.html')