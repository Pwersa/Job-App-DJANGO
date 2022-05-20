from django.contrib import admin
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
######################### Active  ##########################################
    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    path('login_user', views.login_user),
    #path('re_login/<str:username>', views.re_login, name='re_login'),
    path('logout_user', views.logout_user, name='logout_user'),

    path('signup', views.signup, name='signup'),
    path('signup1/<str:username>', views.signup1, name='signup1'),
    path('complete_info', views.complete_info, name='complete_info'),
    path('user_profile/<str:username>', views.user_profile, name='user_profile'),
    path('requirements/<str:username>', views.requirements, name='requirements'),
    path('requirements_satisfied/<str:username_id>', views.requirements_satisfied, name='requirements_satisfied'),
    path('returntoprofile/<str:username>', views.returntoprofile, name='returntoprofile'),

    path('hrdashboard/<str:username_id>', views.hrdashboard, name='hrdashboard'),
    path('manage_account/<str:username>', views.manage_account, name='manage_account'),
    path('change_employment/<str:username>', views.change_employment, name='change_employment'),
    path('sort_list', views.sort_list, name='sort_list'),
    path('set_interview/<str:username_id>', views.set_interview, name="set_interview"),
    path('applicant_hired_reject/<str:username>', views.applicant_hired_reject, name='applicant_hired_reject'),

    path('change_password/<str:username>', views.change_password, name='change_password'),
    path('delete_account/<str:username>', views.delete_account, name='delete_account'),
    
    
############################  UNUSED  ####################################
    
    path('delete', views.delete, name="delete"),
    path('delete_acc', views.delete_acc, name="delete_acc"),
    path('addjob', views.addjob, name="addjob"),
    path('delete_job', views.delete_jobs, name='delete_job'),

############################# DEBUG ########################################
    #path('home_debug', views.home_debug, name='home_debug'),
    #path('login_authenticate', views.login_authenticate, name='login_authenticate'),
    #path('hrdashboard_debug', views.hrdashboard_debug, name='hrdashboard_debug'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)