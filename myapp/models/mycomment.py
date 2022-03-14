from myapp.models.classname import CreateClass
from django.db import models
from django.contrib.auth.models import User


class CommentinClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    myclass = models.ForeignKey(CreateClass, models.CASCADE)
    comment = models.TextField()
