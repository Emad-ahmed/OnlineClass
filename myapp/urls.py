from myapp.forms import AddClassWorkForm
from myapp.views.signup import SignupView
from myapp.views import HomeView
from django.urls import path
from django.contrib import auth
from myapp.forms import MyPasswordResetForm, MySetPasswordForm
from myapp.views import HomeView, SignupView, LoginView, userlogout, CreateView, JoinView, AddclassView, ShowClassworkView, JoinclassView, deletecreateclass, deletejoinclass, AddclassworknewView, pdf_view, mybestcomment, myworkdone, ProfileView, deletemyworkname, editprofile, AssignmentView, PresentationView, ExamInfoView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', userlogout, name='logout'),
    path('deleteclass/<int:id>', deletecreateclass, name='deleteclass'),
    path('deletejoinclass/<int:id>', deletejoinclass, name='deletejoinclass'),
    path('create', CreateView.as_view(), name='create'),
    path('joinclass', JoinView.as_view(), name='joinclass'),
    path('addclass/<int:id>', AddclassView.as_view(), name='addclass'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('showclasswork/<int:id>',
         ShowClassworkView.as_view(), name='showclasswork'),
    path('addclassworknew/<int:id>',
         AddclassworknewView.as_view(), name='addclassworknew'),
    path('joinclassview/<int:id>', JoinclassView.as_view(), name='joinclassview'),
    path('pdf_view/<int:id>', pdf_view, name='pdf_view'),
    path('mybestcomment/<int:id>', mybestcomment, name='mybestcomment'),
    path('myworkdone/<int:id>', myworkdone, name='myworkdone'),
    path('editprofile', editprofile, name='editprofile'),
    path('deletemyworkname/<int:id>', deletemyworkname, name='deletemyworkname'),
    path('assignment', AssignmentView.as_view(), name='assignment'),
    path('presentation', PresentationView.as_view(), name='presentation'),
    path('examinfo', ExamInfoView.as_view(), name='examinfo'),

    # Password Reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),


    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),


    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),


    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
]
