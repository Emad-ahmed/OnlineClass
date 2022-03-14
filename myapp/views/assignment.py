from django.contrib import messages
from myapp.models.mycomment import CommentinClass
from myapp.models.classname import CreateClass
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views import View
from myapp.forms import CreateClassForm, AddClassWorkForm
from myapp.models import CreateClass, JoinClass, AddClassWork, joinclass, CommentinClass, WorkdoneClass, ProfileClass
from django.core.files.storage import FileSystemStorage


# Create your views here.


class AssignmentView(View):
    def get(self, request):

        n = request.session.get("myid")

        createclass = CreateClass.objects.get(pk=n)
        mycl = createclass.class_name

        try:
            myprofile = ProfileClass.objects.get(user=request.user)
        except:
            myprofile = None

        assign_claases = [p for p in AddClassWork.objects.filter(myclass__class_name=mycl) if p.mytopic ==
                          "Assignment"]

        my_all_topic_classes = {
            "assign_claases": assign_claases,
            'myprofile': myprofile
        }

        return render(request, "assignment.html", my_all_topic_classes)
