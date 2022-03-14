from myapp.models import CreateClass, AddClassWork
from django.db import models
from django.contrib.auth.models import User


class WorkdoneClass(models.Model):
    myclass = models.ForeignKey(AddClassWork, models.CASCADE)    
    myfile = models.FileField(upload_to='mywork/', blank=True) 
      
    