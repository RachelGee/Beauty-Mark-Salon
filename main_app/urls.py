# beautymarksalon/urls.py

from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service_index, name='service-index'),
    path('appointments/', views.appointments, name='appointments'),
]

