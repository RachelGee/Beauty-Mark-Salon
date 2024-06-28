# beautymarksalon/urls.py

from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service_index, name='service-index'),
    path('services/<int:service_id>/', views.service_detail, name='service-detail'),
    # path('services/detail', views.service_detail, name='service-detail'),
    path('appointments/', views.appointments, name='appointments'),
    path('gallery/', views.gallery, name='gallery'),
]

