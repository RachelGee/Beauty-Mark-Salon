# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# HOME
def home(request):
    return render(request, 'home.html', {'home': home})

# SERVICES
def service_index(request):
    return render(request, 'services/index.html', {'services': services})

class Service:
    def __init__(self, type, description, cost):
        self.type = type
        self.description = description
        self.cost = cost

services = [
    Service('Blowout', '', 40),
    Service('Womens Cut & Style', '', 60),
    Service('Womens Master Cut & Style', '', 65),
    Service('Mens Cut', '', 35),
    Service('Mens Wash & Scissor Cut', '', 40),
    Service('Lengthy Master Color', '', 200),
    Service('Buzz Master Color', '', 100),
    Service('Fix Your Face', 'Standard makeup', 60),
    Service('Face First', 'Master makeup', 90),
]


# ABOUT
def about(request):
    # Send a simple HTML response
    return render(request, 'about.html')