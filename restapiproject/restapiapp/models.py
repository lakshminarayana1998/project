
from django.db import models
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    dob=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    createddate=models.CharField(max_length=30)
    updateddate=models.CharField(max_length=30)