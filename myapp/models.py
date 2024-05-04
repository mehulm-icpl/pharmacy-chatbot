from django.utils.translation import activate
from django.db import models
# Create your models here.

class Feedback(models.Model):
    Name = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField(max_length=10)  # Adjust the max_length as per your requirements
    Email = models.EmailField()
    Message = models.TextField()

class medicine(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.FloatField()
    Photo = models.CharField(max_length=4036)
