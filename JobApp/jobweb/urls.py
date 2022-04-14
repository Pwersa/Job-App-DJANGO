from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('change_password', views.change_pass, name='changepass'),
    path('hrdashboard', views.hrdashboard, name='hrdashboard'),
    path('delete', views.delete, name="delete"),
    path('delete_acc', views.delete_acc, name="delete_acc"),
    path('addjob', views.addjob, name="addjob"),
    path('profile', views.profile, name='profile'),
    path('changepassword', views.changepass1),
    path('showacc', views.showAccount),
    path('createjobs', views.createJobs),
    path('show_jobs', views.job_show),
    path('login', views.login),
    path('account1', views.showAccount),
    path('createJobs', views.createJobs, name='createJobs'),
    path('delete_job', views.delete_jobs, name='delete_job'),
    path('complete_info', views.completeInfo, name='complete_info'),
    ]