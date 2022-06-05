from django.db import models
from django.contrib.auth.models import User
from myapp.models import CreateClass
from datetime import datetime

Choice_Type = (
    ('Assignment', 'Assignment'),
    ('Presentation', 'Presentation'),
    ('Exam Info', 'Exam Info'),
)


class AddClassWork(models.Model):
    myclass = models.ForeignKey(CreateClass, on_delete=models.CASCADE)
    mytopic = models.CharField(
        max_length=20, choices=Choice_Type, default='Presentation')
    title = models.TextField(max_length=100, default="none")
    description = models.TextField(blank=True)
    imagephoto = models.ImageField(upload_to='images/', blank=True)
    document = models.FileField(upload_to='documents/', blank=True)
    current_date = models.DateTimeField(
        auto_now_add=True,  blank=True)
    end_date_time = models.DateTimeField(auto_now_add=True,
                                         blank=True)

    def __str__(self):
        return self.myclass.class_name
