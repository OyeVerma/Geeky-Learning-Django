from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)