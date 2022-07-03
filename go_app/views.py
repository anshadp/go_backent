from django.shortcuts import render
from django.http import HttpResponse
from .serializers import SignUpSerializer, BusDetailsSerializer, ScheduleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status





# Create your views here.
@csrf_exempt
def signUp(request):
    if request.method == 'POST': 

        userData = JSONParser().parse(request)
        userSerializer = SignUpSerializer(data = userData)

        if userSerializer.is_valid():
            userSerializer.save()
            return JsonResponse({"status": "success", "data": userSerializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": userSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def addBus(request):
    if request.method == 'POST': 

        busData = JSONParser().parse(request)

        busSerializer = BusDetailsSerializer(data = busData)

        if busSerializer.is_valid():
            busSerializer.save()
            return JsonResponse({"status": "success", "data": busSerializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": busSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def addSchedule(request):
    if request.method == 'POST': 

        busData = JSONParser().parse(request)

        scheduleSerializer = ScheduleSerializer(data = busData)

        if scheduleSerializer.is_valid():
            scheduleSerializer.save()
            return JsonResponse({"status": "success", "data": scheduleSerializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": scheduleSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)




