from django.contrib import messages
from myapp.models.mycomment import CommentinClass
from myapp.models.classname import CreateClass
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views import View
from myapp.forms import CreateClassForm, AddClassWorkForm
from myapp.models import CreateClass, JoinClass, AddClassWork, joinclass, CommentinClass, WorkdoneClass, ProfileClass, StudentRegister
from django.core.files.storage import FileSystemStorage
# Create your views here.


# Create your views here.


class PresentationView(View):
    def get(self, request):
        student = request.session.get("student")
        myteach = request.user.is_anonymous
        if not myteach:
            n = request.session.get("myid")

            createclass = CreateClass.objects.get(pk=n)
            mycl = createclass.class_name

            try:
                myprofile = ProfileClass.objects.get(user=request.user)
            except:
                myprofile = None

            assign_claases = [p for p in AddClassWork.objects.filter(myclass__class_name=mycl) if p.mytopic ==
                              "Presentation"]

            my_all_topic_classes = {
                "assign_claases": assign_claases,
                'myprofile': myprofile
            }

            return render(request, "presentation.html", my_all_topic_classes)
        elif myteach:
            student_class = StudentRegister.objects.get(id=student)
            myclass = JoinClass.objects.get(student_user=student_class)
            mycl = myclass.createclass.class_name
            try:
                myprofile = ProfileClass.objects.get(
                    student_user=student_class)
            except:
                myprofile = None

            assign_claases = [p for p in AddClassWork.objects.filter(myclass__class_name=mycl) if p.mytopic ==
                              "Presentation"]

            my_all_topic_classes = {
                "assign_claases": assign_claases,
                'myprofile': myprofile
            }
            return render(request, "presentation.html", my_all_topic_classes)
