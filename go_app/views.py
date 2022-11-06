from .serializers import SignUpSerializer, AccountSerializer, BusDetailsSerializer, ScheduleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from . models import BusDetails, SignUp, Account, Schedule
import jwt
import json
from django.conf import settings


# Create your views here.
@csrf_exempt
def signUp(request):
    try:
        if request.method == 'POST':
            userData = JSONParser().parse(request)

            signUpData = {  
                    'username': userData['username'],
                    'phone_no': userData['phone_no'],
                    'status': userData['status'],
                }

            userSerializer = SignUpSerializer(data = signUpData)
            
            if userSerializer.is_valid():
                userSerializer.save()
                userId = SignUp.objects.get(id=userSerializer.data['id'])
                accountData = {  
                    'email': userData['email'],
                    'Password': userData['password'],
                    'user_type': userData['userType'],
                    'user': userId.id
                } 

            accountSerializer = AccountSerializer(data = accountData)

            if accountSerializer.is_valid():
                accountSerializer.save()
                return JsonResponse({"status": "success", "data": userSerializer.data}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"status": "error", "data": accountSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return JsonResponse({"status": "error", "data": e}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def login(request):
    
    if request.method == 'POST':
        loginCred = JSONParser().parse(request)

        try:
            userDetails = Account.objects.get(email=loginCred['email'])

            userObj = {
                'accountId': userDetails.id,
                'userId': userDetails.user.id,
                'userType': userDetails.user_type,
            }

            decodedUserObj = json.dumps(userObj)

            if userDetails.email == loginCred['email'] and userDetails.Password == loginCred['password']:
                tokenObj = {
                    'userId': userDetails.id
                }
                token = jwt.encode(payload=tokenObj, key=settings.SECRET_KEY, algorithm="HS256")

                return JsonResponse({"status": "success", "token": token, "userDetails": decodedUserObj}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"status": "error", "data": 'Login failed'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return JsonResponse({"status": "error", "data": 'Login failed'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def serveBusDetails(request, id=0):  #continue on this
    
    if request.method == 'POST':
        busData = JSONParser().parse(request)

        busSerializer = BusDetailsSerializer(data = busData)

        if busSerializer.is_valid():
            busSerializer.save()
            
            return JsonResponse({"status": "success", "data": busSerializer.data}, status=status.HTTP_200_OK)
        else:
            print(busSerializer.errors)
            return JsonResponse({"status": "error", "data": busSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        User = BusDetails.objects.filter(user_id=id)
        busSerializer = BusDetailsSerializer(User,many='True')
        return JsonResponse(busSerializer.data,safe=False)


@csrf_exempt
def serveSchedule(request):

    if request.method == 'POST':
        busData = JSONParser().parse(request)
        scheduleSerializer = ScheduleSerializer(data = busData) 

        if scheduleSerializer.is_valid():

            scheduleSerializer.save()
            return JsonResponse({"status": "Schedule added successfully", "data": scheduleSerializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "An error occurred", "data": scheduleSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        schedules = Schedule.objects.all()
        scheduleSerializer = ScheduleSerializer(schedules,many='True')
        return JsonResponse(scheduleSerializer.data,safe=False)


