from rest_framework import serializers
from .models import SignUp, Account, BusDetails, Schedule

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id',  'username', 'phone_no', 'status')


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id',  'email', 'Password', 'user_type', 'user')


class BusDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusDetails
        fields = ('id', 'bus_name', 'bus_no', 'contact', 'user')


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'taking_place', 'reaching_place', 'taking_time', 'reaching_time', 'time_taken', 'bus_id')
