from django.db import models
from django.contrib.auth.models import User
from myapp.models import CreateClass


class JoinClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createclass = models.ForeignKey(CreateClass, on_delete=models.CASCADE)
