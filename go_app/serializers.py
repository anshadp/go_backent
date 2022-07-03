from rest_framework import serializers
from .models import SignUp, BusDetails

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id','email', 'phone_no', 'username', 'password')

class BusDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusDetails
        fields = ('id', 'bus_name', 'bus_no', 'contact', 'private')
