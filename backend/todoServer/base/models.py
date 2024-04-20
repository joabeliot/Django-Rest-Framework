from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=24)
    created = models.DateTimeField(auto_now_add=True)

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title