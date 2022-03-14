from django.http.response import HttpResponseRedirect
from myapp.models.classname import CreateClass
from django.shortcuts import render
from django.views import View
from myapp.forms import CreateClassForm
from myapp.models import ProfileClass
# Create your views here.


class CreateView(View):
    def get(self, request):
        if request.user.is_authenticated:
            my = request.session.get('myteacher')
            fm = CreateClassForm()
            myprofile = ProfileClass.objects.get(user=request.user)
            return render(request, 'create.html', {'form': fm, 'myprofile': myprofile, 'my': my})

        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        fm = CreateClassForm(request.POST)
        my = request.session.get('myteacher')
        if fm.is_valid():
            myuser = request.user
            class_name = fm.cleaned_data['class_name']
            section = fm.cleaned_data['section']
            subject = fm.cleaned_data['subject']
            room = fm.cleaned_data['room']
            classcode = fm.cleaned_data['classcode']
            my = request.session.get('myteacher')
            craeteclassall = CreateClass(user=myuser, class_name=class_name,
                                         section=section, subject=subject, room=room, classcode=classcode)
            craeteclassall.save()
            return render(request, 'create.html', {'form': fm, 'my': my})
