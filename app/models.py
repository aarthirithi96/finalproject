from django.db import models
class Employee(models.Model):
    eid=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=100)




# Create your models here.
