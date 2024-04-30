from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=40)
    no=models.IntegerField()
    role=models.CharField(max_length=40)
    salary=models.FloatField()
    location=models.CharField(max_length=40)
