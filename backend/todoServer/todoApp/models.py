from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=14)

class Task(models.Model):
    statChoice={
        "P":"Pending",
        "IP":"In-Progress",
        "C":"Completed"
    }
    taskName = models.CharField(max_length=50)
    taskDesc = models.CharField(max_length=100)
    taskStat = models.CharField(max_length=1,choices=statChoice)