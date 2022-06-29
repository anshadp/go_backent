from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    # status = models.CharField(max_length=100,default="  ")  
    # created_date = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
