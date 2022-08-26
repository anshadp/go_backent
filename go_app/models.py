from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    status = models.BooleanField(default=True)  
    created_date = models.DateField(auto_now_add=True)


    class Meta():
        db_table = 'signup'


class Account(models.Model):
    email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100,default="Admin")
    user = models.ForeignKey(SignUp, on_delete=models.CASCADE)

    class Meta():
        db_table = 'account_details'



class BusDetails(models.Model):
    bus_name = models.CharField(max_length=100)
    bus_no = models.CharField(max_length=100)
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

    
 





