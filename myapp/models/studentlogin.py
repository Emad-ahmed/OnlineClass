import email
from myapp.models.classname import CreateClass
from django.db import models
from django.contrib.auth.models import User


class StudentRegister(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_password = models.CharField(max_length=250)
    student_cpassword = models.CharField(max_length=250)
