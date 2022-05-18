import imp
from django.db import models
from django.contrib.auth.models import User
from myapp.models.classname import CreateClass
from myapp.models.studentlogin import StudentRegister


class Course(models.Model):
    course_name = models.ForeignKey(CreateClass, on_delete=models.CASCADE)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    cat = (('Option1', 'Option1'), ('Option2', 'Option2'),
           ('Option3', 'Option3'), ('Option4', 'Option4'))
    answer = models.CharField(max_length=200, choices=cat)


class Result(models.Model):
    student_user = models.ForeignKey(
        StudentRegister, on_delete=models.CASCADE, blank=True, null=True)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
