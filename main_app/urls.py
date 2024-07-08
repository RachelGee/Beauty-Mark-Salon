# beautymarksalon/urls.py

from django.urls import path
from . import views # Import views to connect routes to view functions


urlpatterns = [
    # Routes will be added here
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service_index, name='service-index'),
    path('services/<int:service_id>/', views.service_detail, name='service-detail'),
    path('appointments/', views.add_appointment, name='appointments'),
    path('accounts/signup/', views.signup, name='signup')
]

