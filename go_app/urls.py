from django.urls import path, include
from . import views 


urlpatterns = [
    path('user_signup', views.signUp),
    path('login', views.login),
    path('bus_details/<int:id>', views.serveBusDetails),
    path('bus_details', views.serveBusDetails),
    path('schedule_details', views.serveSchedule, name='add_schedule')
]