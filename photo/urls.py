from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage, name='home'),
    path('about/', AboutPage, name='about'),
    path('contact/', ContactPage, name='contact'),
    path('thanks/', ThankYouView.as_view(), name='thanks'),
    path('info/', InfoPage, name='info'),
    path('seniors/', SeniorsPage, name='seniors'),
    path('portraits/', PortraitsPage, name='portraits'),
    path('weddings/', WeddingsPage, name='weddings'),
    path('drone/', DronePage, name='drones'),
    path('resume/', resume, name='resume'),
    #path('clients/', ClientPage, name='clients'),
]
