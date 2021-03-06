from myapp.models.examquestion import Course
from myapp.models.myprofile import ProfileClass
from django.contrib.auth.models import User

from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from myapp.models import CreateClass, JoinClass, ProfileClass
from django.contrib.auth.forms import User
from myapp.forms import ProfileForm, EditProfileForm, CourseForm, AddQuestionForm
from django.contrib import messages
from myapp.models.examquestion import Course
# Create your views here.


class AddQuizView(View):
    def get(self, request):
        fm = CourseForm()
        return render(request, 'add_quiz.html', {'form': fm})

    def post(self, request):
        n = request.session.get("myid")
        createclass = CreateClass.objects.get(pk=n)
        fm = CourseForm(request.POST)
        if fm.is_valid():

            obj = fm.save(commit=False)
            obj.course_name = createclass
            obj.save()
            myid = obj.id
            return redirect('add_question', id=myid)
        else:
            return render(request, 'add_quiz.html', {'form': fm})


class Add_Quiz_Question_View(View):
    def get(self, request, id):
        fm = AddQuestionForm()
        mycourse = Course.objects.get(id=id)
        mytotal = mycourse.question_number

        return render(request, "add_quiz_question.html", {'form': fm, 'mytotal': mytotal})

    def post(self, request, id):
        mycourse = Course.objects.get(id=id)
        mymark = mycourse.total_marks
        mytotal = mycourse.question_number
        print(mytotal)
        for i in range(mytotal):
            fm = AddQuestionForm(request.POST)

        if fm.is_valid():
            for i in range(mytotal):
                obj = fm.save(commit=False)
                obj.course = mycourse
                obj.marks = mymark
                obj.save()

        return render(request, "add_quiz_question.html", {'form': fm, 'mytotal': mytotal})
