from django.db import models
from django.contrib.auth.models import User


class CreateClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    classcode = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name
