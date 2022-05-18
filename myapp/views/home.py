from myapp.models.myprofile import ProfileClass
from django.contrib.auth.models import User
from myapp.models.addwork import AddClassWork
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myapp.models import CreateClass, JoinClass, ProfileClass
from django.contrib.auth.forms import User
from django.contrib import messages
# Create your views here.


class HomeView(View):
    def get(self, request):

        my = request.session.get('myteacher')
        myallclass = CreateClass.objects.filter(user=request.user)
        newclass = JoinClass.objects.filter(user=request.user)
        addmyclass = AddClassWork.objects.filter(
            myclass__user=request.user).last()
        try:
            myprofile = ProfileClass.objects.get(user=request.user)
        except:
            return render(request, 'home.html', {'allclass': myallclass, 'newclass': newclass, 'addmyclass': addmyclass, 'my': my})
        return render(request, 'home.html', {'allclass': myallclass, 'newclass': newclass, 'addmyclass': addmyclass, 'my': my, 'myprofile': myprofile})


class JoinView(View):
    def get(self, request):
        my = request.session.get('myteacher')
        try:
            myprofile = ProfileClass.objects.get(user=request.user)
        except:
            return render(request, 'joinclass.html')
        return render(request, 'joinclass.html', {'myprofile': myprofile, 'my': my})

    def post(self, request):
        my = request.session.get('myteacher')
        joinclass = request.POST.get('joinclass')
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


def deletecreateclass(request, id):
    deleteclass = CreateClass.objects.get(pk=id)
    deleteclass.delete()
    return HttpResponseRedirect('/')


def deletejoinclass(request, id):
    deleteclass = JoinClass.objects.get(pk=id)
    deleteclass.delete()
    return HttpResponseRedirect('/')
