from django.urls import path, include
from .views import BusDataView, ScheduleDataView, SignUpView


urlpatterns = [
    path('add_bus', SignUpView.as_view()),
    path('add_bus', BusDataView.as_view()),
    path('add_schedule', ScheduleDataView.as_view(), name='add_schedule')

    

]