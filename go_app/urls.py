from django.urls import path, include
from . import views

urlpatterns = [
    path('first', views.serveLogin, name='first')
]