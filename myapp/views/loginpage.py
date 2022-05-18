from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from myapp.forms import LoginForm, StudentRegisterForm
from django.contrib.auth import authenticate, login, logout
from myapp.models import ProfileClass
from django.contrib import messages
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
        return render(request, 'student-register.html', {'form': fm})

    def post(self, request):
        fm = StudentRegisterForm(request.POST)
        return render(request, 'student-register', {'form': fm})


class LoginstudentView(View):
    def get(self, request):
        return render(request, 'loginstu.html')
