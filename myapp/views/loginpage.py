from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from myapp.forms import LoginForm, StudentRegisterForm
from django.contrib.auth import authenticate, login, logout
from myapp.models import ProfileClass
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from myapp.models.studentlogin import StudentRegister
# Create your views here.


class LoginView(View):
    def get(self, request):
        fm = LoginForm()

        return render(request, 'login.html', {'form': fm, 'myhover': 'active'})

    def post(self, request):
        fm = LoginForm(request=request, data=request.POST)

        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            myteacher = request.POST.get('selected_value')
            request.session['myteacher'] = myteacher
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

        messages.warning(request, 'Email Or Password Invalid')
        return render(request, 'login.html', {'form': fm})


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('login')


class Studentre(View):
    def get(self, request):
        fm = StudentRegisterForm()
        return render(request, 'student-register.html', {'form': fm, 'myhover': 'active'})

    def post(self, request):
        fm = StudentRegisterForm(request.POST)
        if fm.is_valid():
            student_password = fm.cleaned_data['student_password']
            student_cpassword = fm.cleaned_data['student_cpassword']
            mypassword = make_password(student_password)
            mypassword1 = make_password(student_cpassword)
            obj = fm.save(commit=False)
            obj.student_password = mypassword
            obj.student_cpassword = mypassword1
            obj.save()
        return render(request, 'student-register.html', {'form': fm, 'myhover': 'active'})


class LoginstudentView(View):
    return_url = None

    def get(self, request):
        LoginstudentView.return_url = request.GET.get('return_url')
        return render(request, 'loginstu.html', {'myhover': 'active'})

    def post(self, request):
        student_id = request.POST.get('id_no')
        password = request.POST.get('password')

        student = StudentRegister.get_student_by_id(student_id)

        if student:
            flag = check_password(password, student.student_password)
            if flag:
                request.session['student'] = student.id
                if LoginstudentView.return_url:
                    return HttpResponseRedirect(LoginView.return_url)
                else:
                    LoginstudentView.return_url = None
                    return redirect('/')
            else:
                error_message = 'Id no or Password invalid !!'
        else:
            error_message = 'Id No or Password invalid !!'

        return render(request, 'loginstu.html', {'error': error_message})
