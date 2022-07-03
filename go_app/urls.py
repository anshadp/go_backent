from django.urls import path, include
from . import views

urlpatterns = [
    path('first', views.signUp, name='first'),
    path('add_bus', views.addBus, name='add_bus'),
    path('add_schedule', views.addSchedule, name='add_schedule')

    

]