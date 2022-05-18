from myapp.models.classname import CreateClass
from django.db import models
from django.contrib.auth.models import User

from myapp.models.studentlogin import StudentRegister


class CommentinClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_user = models.OneToOneField(
        StudentRegister, on_delete=models.CASCADE, blank=True, null=True)
    myclass = models.ForeignKey(CreateClass, models.CASCADE)
    comment = models.TextField()
