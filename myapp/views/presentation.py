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


class PresentationView(View):
    def get(self, request):
        from django.contrib import messages


# Create your views here.


class PresentationView(View):
    def get(self, request):

        n = request.session.get("myid")
        try:
            myprofile = ProfileClass.objects.get(user=request.user)
        except:
            myprofile = None

        createclass = CreateClass.objects.get(pk=n)
        mycl = createclass.class_name

        present_classes = [p for p in AddClassWork.objects.filter(myclass__class_name=mycl) if p.mytopic ==
                           "Presentation"]

        my_all_topic_classes = {
            "presentation_claases": present_classes,
            'myprofile': myprofile
        }

        return render(request, "presentation.html", my_all_topic_classes)
