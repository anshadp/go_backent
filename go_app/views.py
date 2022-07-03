from django.shortcuts import render
from django.http import HttpResponse
from .serializers import SignUpSerializer, BusDetailsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status





# Create your views here.
@csrf_exempt
def serveSignUp(request):
    if request.method == 'POST': 

        userData = JSONParser().parse(request)
        userSerializer = SignUpSerializer(data = userData)

        if userSerializer.is_valid():
            userSerializer.save()
            return JsonResponse({"status": "success", "data": userSerializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": userSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def serveBus(request):
    if request.method == 'POST': 

        busData = JSONParser().parse(request)

        busSerializer = BusDetailsSerializer(data = busData)

        if busSerializer.is_valid():
            busSerializer.save()
            return JsonResponse({"status": "success", "data": busSerializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": busSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)





