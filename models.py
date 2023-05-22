from django.db import models

# Create your models here.

class Person(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)


