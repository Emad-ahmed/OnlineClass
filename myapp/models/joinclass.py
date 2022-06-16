from django.db import models
from django.contrib.auth.models import User
from myapp.models import CreateClass
from myapp.models.studentlogin import StudentRegister


class JoinClass(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    student_user = models.ForeignKey(
        StudentRegister, on_delete=models.CASCADE, blank=True, null=True)
    createclass = models.ForeignKey(CreateClass, on_delete=models.CASCADE)
