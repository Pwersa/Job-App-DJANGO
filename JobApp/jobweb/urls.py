from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('change_password', views.change_pass, name='changepass'),
    path('hrdashboard', views.hrdashboard, name='hrdashboard'),
    #path('employee', views.employee, name='employee'),
    #path('applicant', views.applicant, name='applicant'),
    path('emp_amp', views.emp_apm, name="emp_amp"),

    path('addjob', views.addjob, name="addjob"),
    path('profile', views.profile, name='profile'),

    path('changepassword', views.changepass1),
    path('admin/', admin.site.urls),
    path('createacc', views.createAccount),
    path('showacc', views.showAccount),

    path('createjobs', views.createJobs),
    path('showjobs', views.showJobs),

    path('login', views.login),
    path('account1', views.showAccount),

    ]