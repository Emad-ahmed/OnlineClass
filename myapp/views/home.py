from tkinter.messagebox import NO
from myapp.models.myprofile import ProfileClass
from django.contrib.auth.models import User
from myapp.models import AddClassWork, StudentRegister
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myapp.models import CreateClass, JoinClass, ProfileClass
from django.contrib.auth.forms import User
from django.contrib import messages
from django.db.models import Q
# Create your views here.


class HomeView(View):
    def get(self, request):

        student = request.session.get("student")
        myteach = request.user.is_anonymous

        if not myteach:
            myallclass = CreateClass.objects.filter(user=request.user)
            newclass = JoinClass.objects.filter(user=request.user)
            addmyclass = AddClassWork.objects.filter(
                myclass__user=request.user).last()
            try:
                myprofile = ProfileClass.objects.get(user=request.user)
            except:
                return render(request, 'home.html', {'allclass': myallclass, 'newclass': newclass, 'addmyclass': addmyclass})
            return render(request, 'home.html', {'allclass': myallclass, 'newclass': newclass, 'addmyclass': addmyclass, 'myprofile': myprofile})
        elif myteach:
            try:
                st = StudentRegister.objects.get(pk=student)

            except:
                st = None
            newclass = JoinClass.objects.filter(student_user=st)

            return render(request, 'home.html', {'newclass': newclass, "n": st, "student": student})

        else:
            return HttpResponseRedirect("/login")


class JoinView(View):
    def get(self, request):
        student = request.session.get("student")
        myteach = request.user.is_anonymous
        if not myteach:
            my = request.session.get('myteacher')
            try:
                myprofile = ProfileClass.objects.get(user=request.user)
            except:
                return render(request, 'joinclass.html')
            return render(request, 'joinclass.html', {'myprofile': myprofile, 'my': my})
        elif myteach:
            try:
                st = StudentRegister.objects.get(pk=student)
            except:
                st = None
            try:
                myprofile = ProfileClass.objects.get(student_user=st)
            except:
                return render(request, 'joinclass.html')
            return render(request, 'joinclass.html', {'myprofile': myprofile, 'my': my})

    def post(self, request):
        student = request.session.get("student")
        myteach = request.user.is_anonymous
        my = request.session.get('myteacher')
        joinclass = request.POST.get('joinclass')
        if not myteach:
            try:
                newclass = CreateClass.objects.get(classcode=joinclass)
            except:
                messages.success(request, "Enter Correct Classcode")
                return HttpResponseRedirect('/joinclass')

            myjoin = JoinClass(user=request.user, createclass=newclass)

            alljoinclass = JoinClass.objects.filter(user=request.user)

            mycreateclass = CreateClass.objects.filter(user=request.user)

            for myclass in alljoinclass:
                if myclass.createclass.classcode == joinclass:
                    messages.success(request, "Class Already Exists")
                    return HttpResponseRedirect("/joinclass")

            for myclass in mycreateclass:
                if myclass.classcode == joinclass:
                    messages.success(request, "Class Already Exists")
                    return HttpResponseRedirect("/joinclass")

            myjoin.save()
            return HttpResponseRedirect('/')

        elif myteach:
            try:
                st = StudentRegister.objects.get(pk=student)
                newclass = CreateClass.objects.get(classcode=joinclass)
            except:
                messages.success(request, "Enter Correct Classcode")
                return HttpResponseRedirect('/joinclass')

            myjoin = JoinClass(student_user=st, createclass=newclass)

            alljoinclass = JoinClass.objects.filter(student_user=st)

            for myclass in alljoinclass:
                if myclass.createclass.classcode == joinclass:
                    messages.success(request, "Class Already Exists")
                    return HttpResponseRedirect("/joinclass")

            myjoin.save()
            return HttpResponseRedirect('/')


def deletecreateclass(request, id):
    deleteclass = CreateClass.objects.get(pk=id)
    deleteclass.delete()
    return HttpResponseRedirect('/')


def deletejoinclass(request, id):
    deleteclass = JoinClass.objects.get(pk=id)
    deleteclass.delete()
    return HttpResponseRedirect('/')
