from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=250)
    course = models.CharField(max_length=20)
    phone_number = models.IntegerField()


class Faculty(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=250)
    subject = models.CharField(max_length = 30)
    phone_number = models.IntegerField()
