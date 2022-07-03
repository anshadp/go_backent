from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta():
        db_table = 'SignUp'


class BusDetails(models.Model):
    busName = models.CharField(max_length=100)
    busNo = models.IntegerField()
    route = models.CharField(max_length=100)

    class Meta():
        db_table = 'bus_details'


class Timing(models.Model):
    takingPlace = models.CharField(max_length=100)
    reachingPlace = models.CharField(max_length=100)
    takingTime = models.TimeField()
    reachingTime = models.TimeField()
    timeTaken = models.CharField(max_length=100)
    busId = models.ForeignKey(BusDetails, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('takingTime', 'busId'))
        db_table = 'bus_times'

    
 





