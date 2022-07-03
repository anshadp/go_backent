from django.urls import path, include
from . import views

urlpatterns = [
    path('first', views.serveSignUp, name='first')
]