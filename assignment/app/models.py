from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Work(models.Model):
    workType = (
        ('YT','Youtube'),
        ('IG','Instagram'),
        ('OT' , 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(max_length=2,choices=workType)

    def __str__(self):
        return self.link


class Artist(models.Model):
    name = models.CharField(max_length=255)
    work = models.ManyToManyField(Work,related_name='artist')

    def __str__(self):
        return self.name