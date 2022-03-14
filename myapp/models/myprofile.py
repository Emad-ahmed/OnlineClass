from myapp.models.classname import CreateClass
from django.db import models
from django.contrib.auth.models import User


class ProfileClass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    myimage = models.ImageField(upload_to='profile/', blank=True)
