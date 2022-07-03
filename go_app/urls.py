from django.urls import path, include
from . import views

urlpatterns = [
    path('first', views.serveSignUp, name='first'),
    path('add_bus', views.serveBus, name='add_bus')

]