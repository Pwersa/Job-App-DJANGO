from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('hrdashboard', views.hrdashboard, name='hrdashboard'),
    path('employee', views.employee, name='employee'),
    path('applicant', views.applicant, name='applicant'),
    path('addjob', views.addjob, name="addjob"),
    path('profile', views.profile, name='profile'),

    path('admin/', admin.site.urls),
    path('createacc', views.createAccount),
    path('showacc', views.showAccount),
    ]