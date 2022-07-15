from django.urls import path, include
from .views import BusDataView

urlpatterns = [
    # path('first', views.signUp, name='first'),
    path('add_bus', BusDataView.as_view()),
    path('add_schedule', views.addSchedule, name='add_schedule')

    

]