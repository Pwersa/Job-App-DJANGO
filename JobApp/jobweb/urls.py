from django.contrib import admin
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
######################## WEBSITE ###########################

    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login_user', views.login_user),
    path('logout_user', views.logout_user, name='logout_user'),
    path('signup', views.signup, name='signup'),
    path('signup1/<str:username>/account_finished?=<str:verified_user>', views.signup1, name='signup1'),

########################### APPLICANT//EMPLOYEE ###########################

    path('user_profile/<str:username>/verified_user?=<str:verified_user>', views.user_profile, name='user_profile'),
    path('returntoprofile/<str:username>', views.returntoprofile, name='returntoprofile'),
    path('requirements/<str:username>/verified_user?=<str:verified_user>', views.requirements, name='requirements'),
    path('requirements_satisfied/<str:username_id>', views.requirements_satisfied, name='requirements_satisfied'),
    path('applicant_level1/<str:username>/not_verified', views.applicant_level1, name='applicant_level1'),
    path('applicant_level_2_3_employee/<str:username>/verified_user?=<str:verified_user>', views.applicant_level_2_3_employee, name='applicant_level_2_3_employee'),
    path('rejected_user/<str:username>', views.rejected_user, name='rejected_user'),
    path('retired_user/<str:username>', views.retired_user, name='retired_user'),
    path('terminated_user/<str:username>', views.terminated_user, name='terminated_user'),
    
######################## HR MANAGER ###########################

    path('hrdashboard/<str:username>/authorized_account?=<str:verified_user>', views.hrdashboard, name='hrdashboard'),
    path('delete_account/<str:username>/verified_user?=<str:verified_user>', views.delete_account, name='delete_account'),
    path('manage_account/<str:username>/verified_user?=<str:verified_user>', views.manage_account, name='manage_account'),
    path('sort_list', views.sort_list, name='sort_list'),
    path('set_interview/<str:username_id>/verified_user?=<str:verified_user>', views.set_interview, name="set_interview"),
    path('change_employment/<str:username>/verified_user?=<str:verified_user>', views.change_employment, name='change_employment'),
    path('applicant_hired_reject/<str:username>/verified_user?=<str:verified_user>', views.applicant_hired_reject, name='applicant_hired_reject'),
    path('manage_joblisting/<str:username>/authorized_account?=<str:verified_user>/create+or+delete+job+listed', views.manage_joblisting, name='manage_joblisting'),
    path('list_job/<str:username>/authorized_account?=<str:verified_user>', views.list_job, name='list_job'),
    path('delete_job/<str:username>/authorized_account?=<str:verified_user>', views.delete_job, name='delete_job'),
    path('email_notify/<str:username>/', views.email_notify, name='email_notify'),
    path('email_send', views.email_send, name='email_send'),
    
######################## GLOBAL ###########################

    path('change_password/<str:username>/verified_user?=<str:verified_user>', views.change_password, name='change_password'),
    path('applicant_employee_create_pdf/<str:username>', views.applicant_employee_create_pdf, name='applicant_employee_create_pdf'),
    path('export_as_csv', views.export_as_csv, name='export_as_csv'),
    
############################# DEBUG ########################################

    #path('home_debug', views.home_debug, name='home_debug'),
    #path('login_authenticate', views.login_authenticate, name='login_authenticate'),
    path('hrdashboard_debug/<str:username>/authorized_account?=<str:verified_user>', views.hrdashboard_debug, name='hrdashboard_debug'),
    path('hrdashboard_debug', views.hrdashboard_debug, name='hrdashboard_debug'),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)