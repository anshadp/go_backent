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
    bus_name = models.CharField(max_length=100)
    bus_no = models.IntegerField()
    contact = models.BigIntegerField()
    private = models.BooleanField()

    class Meta():
        db_table = 'bus_details'


class Schedule(models.Model):
    taking_place = models.CharField(max_length=100)
    reaching_place = models.CharField(max_length=100)
    taking_time = models.TimeField()
    reaching_time = models.TimeField()
    time_taken = models.CharField(max_length=100)
    bus_id = models.ForeignKey(BusDetails, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('taking_time', 'bus_id'))
        db_table = 'bus_schedule'

    
 





