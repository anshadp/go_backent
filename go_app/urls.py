from django.urls import path, include
from . import views 


urlpatterns = [
    path('user_signup', views.signUp),
    path('login', views.login),
    path('add_bus', views.serveBusDetails),
    path('add_schedule', views.serveSchedule, name='add_schedule')
]