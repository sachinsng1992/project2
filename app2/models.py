from django.db import models

class Employee(models.Model):
    username =models.CharField(max_length=20)
    password =models.CharField(max_length=8)
    type = models.CharField(max_length=10)
