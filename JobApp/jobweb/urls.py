from django.contrib import admin
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
######################### Active  ##########################################
    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    path('login', views.login),
    path('re_login', views.re_login),

    path('signup', views.signup, name='signup'),
    path('signup1', views.signup1, name='signup1'),
    path('complete_info', views.complete_info, name='complete_info'),
    path('user_profile', views.user_profile, name='user_profile'),

    path('hrdashboard', views.hrdashboard, name='hrdashboard'),
    path('delete_account', views.delete_account, name='delete_account'),

############################  UNUSED  ####################################
    path('change_password', views.change_pass, name='changepass'),
    path('delete', views.delete, name="delete"),
    path('delete_acc', views.delete_acc, name="delete_acc"),
    path('addjob', views.addjob, name="addjob"),
    path('changepassword', views.changepass1),
    path('showacc', views.showAccount),
    path('createjobs', views.createJobs),
    path('show_jobs', views.job_show),
    path('account1', views.showAccount),
    path('createJobs', views.createJobs, name='createJobs'),
    path('delete_job', views.delete_jobs, name='delete_job'),

############################# DEBUG ########################################
    path('home_debug', views.home_debug, name='home_debug'),
    path('hrdashboard_debug', views.hrdashboard_debug, name='hrdashboard_debug'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    