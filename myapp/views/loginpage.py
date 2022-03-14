from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from myapp.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from myapp.models import ProfileClass
from django.contrib import messages
# Create your views here.


class LoginView(View):
    def get(self, request):
        fm = LoginForm()

        return render(request, 'login.html', {'form': fm})

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
