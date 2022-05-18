from myapp.models.classname import CreateClass
from django.db import models
from django.contrib.auth.models import User
from myapp.models.studentlogin import StudentRegister


class ProfileClass(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    student_user = models.OneToOneField(
        StudentRegister, on_delete=models.CASCADE, blank=True, null=True)
    myimage = models.ImageField(upload_to='profile/', blank=True)
