from myapp.models.myprofile import ProfileClass
from django.contrib.auth.models import User

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myapp.models import CreateClass, JoinClass, ProfileClass
from django.contrib.auth.forms import User
from myapp.forms import ProfileForm, EditProfileForm
from django.contrib import messages
# Create your views here.


class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            fm = ProfileForm()
            my = request.session.get('myteacher')
            try:
                myprofile = ProfileClass.objects.get(user=request.user)
            except:
                return render(request, 'profile.html', {'form': fm, 'my': my})

            return render(request, 'profile.html', {'form': fm, 'myprofile': myprofile, 'my': my})

    def post(self, request):
        fm = ProfileForm(request.POST, request.FILES)
        my = request.session.get('myteacher')
        if fm.is_valid():
            myimage = fm.cleaned_data['myimage']
            print(myimage)
            mypro = ProfileClass(user=request.user, myimage=myimage)
            mypro.save()
            messages.success(request, "Successfully Added Profile Image")
            myprofile = ProfileClass.objects.get(user=request.user)
            return HttpResponseRedirect("/")
        return render(request, 'profile.html', {'form': fm})


def editprofile(request):
    if request.user.is_authenticated:
        try:
            my = request.session.get('myteacher')

            myprofile = ProfileClass.objects.get(user=request.user)

            if request.method == "POST":
                fm = EditProfileForm(request.POST, instance=request.user)
                if fm.is_valid():
                    fm.save()

            else:
                fm = EditProfileForm(instance=request.user)
            return render(request, "editprofile.html", {'form': fm, 'myprofile': myprofile})
        except:
            my = request.session.get('myteacher')

            if request.method == "POST":
                fm = EditProfileForm(request.POST, instance=request.user)
                if fm.is_valid():
                    fm.save()

            else:
                fm = EditProfileForm(instance=request.user)
            return render(request, "editprofile.html", {'form': fm})
    else:
        return HttpResponseRedirect("/login")
