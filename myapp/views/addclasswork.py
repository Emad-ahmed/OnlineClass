from django.contrib import messages
from myapp.models.mycomment import CommentinClass
from myapp.models.classname import CreateClass
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views import View
from myapp.forms import CreateClassForm, AddClassWorkForm
from myapp.models import CreateClass, JoinClass, AddClassWork, joinclass, CommentinClass, WorkdoneClass, ProfileClass
from django.core.files.storage import FileSystemStorage

from myapp.models.studentlogin import StudentRegister
# Create your views here.


class AddclassView(View):
    def get(self, request, id):
        student = request.session.get("student")
        myteach = request.user.is_anonymous
        if not myteach:
            request.session['myid'] = id
            myclass = CreateClass.objects.get(pk=id)
            classcode = myclass.classcode
            myname = myclass.user
            print(myname)

            addclass = AddClassWork.objects.filter(
                myclass__classcode=classcode)

            myjoinclass = JoinClass.objects.filter(
                createclass__classcode=classcode)

            try:
                myprofile = ProfileClass.objects.get(user=request.user)
            except:
                return render(request, 'addclasswork.html', {'addclass': addclass, 'myclass': myclass, 'myname': myname, 'myjoinclass': myjoinclass})

            return render(request, 'addclasswork.html', {'addclass': addclass, 'myclass': myclass, 'myname': myname, 'myjoinclass': myjoinclass, 'myprofile': myprofile})
        elif myteach:
            student_class = StudentRegister.objects.get(id=student)
            myclass = JoinClass.objects.get(student_user=student_class)
            classcode = myclass.createclass.classcode
            myjoinclass = JoinClass.objects.filter(
                createclass__classcode=classcode)

            try:
                myprofile = ProfileClass.objects.get(
                    student_user=student_class)
            except:
                return render(request, 'addclasswork.html', {'myclass': myclass,  'myjoinclass': myjoinclass})

            return render(request, 'addclasswork.html', {'myclass': myclass,  'myjoinclass': myjoinclass, 'myprofile': myprofile})


class JoinclassView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            myclass = JoinClass.objects.get(pk=id)
            classcode = myclass.createclass.classcode

            addclass = AddClassWork.objects.filter(
                myclass__classcode=classcode)

            try:
                myprofile = ProfileClass.objects.get(user=request.user)
            except:
                return render(request, 'addclasswork.html', {'addclass': addclass, 'myclass1': myclass})

            return render(request, 'addclasswork.html', {'addclass': addclass, 'myclass1': myclass, 'myprofile': myprofile})
        else:
            return HttpResponseRedirect('/')


class ShowClassworkView(View):
    def get(self, request, id):

        if request.user.is_authenticated:

            showclass = AddClassWork.objects.get(pk=id)
            showcomment = CommentinClass.objects.filter(
                myclass=showclass.myclass)
            try:
                myprofile = ProfileClass.objects.get(user=request.user)
                print(myprofile)
                myworkname = WorkdoneClass.objects.get(myclass=showclass)
            except:
                return render(request, 'showclasswork.html', {'showclass': showclass, 'showcomment': showcomment, "myprofile": myprofile})

            return render(request, 'showclasswork.html', {'showclass': showclass, 'showcomment': showcomment, 'myworkname': myworkname, "myprofile": myprofile})
        else:
            return HttpResponseRedirect('/')


class AddclassworknewView(View):
    def get(self, request, id):
        if request.user.is_authenticated:

            fm = AddClassWorkForm()
            try:
                myprofile = ProfileClass.objects.get(user=request.user)
            except:
                return render(request, 'addmyclass.html', {'form': fm})

            return render(request, 'addmyclass.html', {'form': fm,  'myprofile': myprofile})

        else:
            return HttpResponseRedirect('/')

    def post(self, request, id):

        fm = AddClassWorkForm(request.POST, request.FILES)
        try:
            myprofile = ProfileClass.objects.get(user=request.user)
        except:
            return render(request, 'addmyclass.html', {'form': fm})
        myclass = request.session.get('myid')
        print(myclass)
        classbyid = CreateClass.objects.get(pk=myclass)
        print(classbyid)

        if fm.is_valid():
            mytopic = fm.cleaned_data['mytopic']
            description = fm.cleaned_data['description']
            imagephoto = fm.cleaned_data['imagephoto']
            document = fm.cleaned_data['document']

            myviewclass = AddClassWork(mytopic=mytopic,
                                       myclass=classbyid, description=description, imagephoto=imagephoto, document=document)
            myviewclass.save()

        messages.success(request, 'Added Successfully')
        return render(request, 'addmyclass.html', {'form': fm, 'myprofile': myprofile})


def pdf_view(request, id):
    if request.user.is_authenticated:
        maindata = AddClassWork.objects.get(pk=id)
        mainfile = maindata.document

        fs = FileSystemStorage()
        filename = str(mainfile)

        if fs.exists(filename):
            with fs.open(filename) as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                # user will be prompted display the PDF in the browser
                response['Content-Disposition'] = 'inline; filename="filename"'

                return response
        else:
            return HttpResponseNotFound('The requested pdf was not found in our server.')

    else:
        return HttpResponseRedirect('/')


def mybestcomment(request, id):
    if request.user.is_authenticated:
        showclass = AddClassWork.objects.get(pk=id)
        user = request.user
        myclass = showclass.myclass

        showcomment = CommentinClass.objects.filter(myclass=showclass.myclass)
        try:
            myprofile = ProfileClass.objects.get(user=request.user)
        except:
            return render(request, 'showclasswork.html', {'showclass': showclass, 'showcomment': showcomment})

        if request.method == "POST":
            mybestcomment = request.POST.get('comment')
            mynewcomment = CommentinClass(
                user=user, myclass=myclass, comment=mybestcomment)
            mynewcomment.save()

    else:
        return HttpResponseRedirect("/")

    return render(request, 'showclasswork.html', {'showclass': showclass, 'showcomment': showcomment,  'myprofile': myprofile})


def myworkdone(request, id):
    if request.user.is_authenticated:
        showclass = AddClassWork.objects.get(pk=id)
        showcomment = CommentinClass.objects.filter(myclass=showclass.myclass)
        myworkalready = WorkdoneClass.objects.filter(
            myclass=showclass).exists()

        try:
            myprofile = ProfileClass.objects.get(user=request.user)

            print(myworkalready)
            if request.method == 'POST' and request.FILES['myfile']:
                myfile = request.FILES['myfile']

            if not myworkalready:
                mywork = WorkdoneClass(myclass=showclass, myfile=myfile)
                mywork.save()

                messages.success(request, 'Your Work Submitted Successfully')

        except:
            return render(request, 'showclasswork.html', {'showclass': showclass, 'showcomment': showcomment})
        myworkname = WorkdoneClass.objects.get(myclass=showclass)
        return render(request, 'showclasswork.html', {'showclass': showclass, 'showcomment': showcomment,  'myprofile': myprofile, 'myworkname': myworkname})


def deletemyworkname(request, id):
    if request.user.is_authenticated:
        mywork = WorkdoneClass.objects.get(pk=id)
        mywork.delete()
        messages.success(request, 'Delete Successfully')
        return redirect('/')
