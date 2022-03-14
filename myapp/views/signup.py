from django.shortcuts import render
from django.views import View
from myapp.forms import SignForm
from django.contrib import messages
# Create your views here.


class SignupView(View):
    def get(self, request):
        fm = SignForm()
        return render(request, 'signup.html', {'form': fm})

    def post(self, request):
        fm = SignForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Saved  successfully!')
            fm.save()

        return render(request, 'signup.html', {'form': fm})
