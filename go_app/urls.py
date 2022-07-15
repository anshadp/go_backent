from django.urls import path, include
from .views import BusDataView, ScheduleDataView


urlpatterns = [
    # path('first', views.signUp, name='first'),
    path('add_bus', BusDataView.as_view()),
    path('add_schedule', ScheduleDataView.as_view(), name='add_schedule')

    

]