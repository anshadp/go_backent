from .serializers import SignUpSerializer, BusDetailsSerializer, ScheduleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from . models import BusDetails, SignUp
import jwt
from django.conf import settings


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
def login(request):
    
    if request.method == 'POST':
        loginCred = JSONParser().parse(request)

        try:
            userDetails = SignUp.objects.get(email=loginCred['email'])

            if userDetails.email == loginCred['email'] and userDetails.password == loginCred['password']:

                tokenObj = {
                    'userId': userDetails.id
                }

                token = jwt.encode(payload=tokenObj, key=settings.SECRET_KEY, algorithm="HS256")

                return JsonResponse({"status": "success", "token": token}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"status": "error", "data": 'Login failed'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({"status": "error", "data": 'Login failed'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def serveBusDetails(request):
    
    if request.method == 'POST':
        busData = JSONParser().parse(request)

        busSerializer = BusDetailsSerializer(data = busData)

        if busSerializer.is_valid():
            busSerializer.save()
            return JsonResponse({"status": "success", "data": busSerializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": busSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        User = BusDetails.objects.all()
        busSerializer = BusDetailsSerializer(User,many='True')
        return JsonResponse(busSerializer.data,safe=False)



def serveSchedule(request):

    if request.method == 'POST':
        busData = JSONParser().parse(request)

        scheduleSerializer = ScheduleSerializer(data = busData)

        if scheduleSerializer.is_valid():
            scheduleSerializer.save()
            return JsonResponse({"status": "success", "data": scheduleSerializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "data": scheduleSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)





