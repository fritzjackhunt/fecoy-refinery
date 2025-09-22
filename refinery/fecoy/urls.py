from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('services', views.services, name='services'),
    path('terminals', views.terminals, name='terminals'),
    path('contact', views.contact, name='contact'),
]