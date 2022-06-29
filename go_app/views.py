from django.shortcuts import render
from django.http import HttpResponse
from .serializers import SignUpSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status





# Create your views here.
@csrf_exempt
def serveLogin(request):


    if request.method=='POST':

        userData = JSONParser().parse(request)

        user_serializer = SignUpSerializer(data = userData)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse({"status": "success", "data": user_serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




