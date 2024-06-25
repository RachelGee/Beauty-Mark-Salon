# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# HOME
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello, Beautiful</h1>')

# SERVICES
def services(request):
    # Send a simple HTML response
    return render(request, 'services.html')
