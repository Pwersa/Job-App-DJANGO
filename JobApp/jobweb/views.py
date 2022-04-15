from django.shortcuts import render, redirect
from django.http import HttpResponse
import mysql.connector
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import first_registration
from .models import *
from django.views.decorators.cache import cache_control


######################## ACTIVE #########################

user_email = []
user_account_type = []


def home(request):
    user_email.clear()
    user_account_type.clear()
    data = job_listing.objects.all()
    context = {'job': data}
    return render(request, 'html_files/HOMEWEBSITE.html', context)

def login(request):
    
    check_email = request.POST['email1']
    data = account_registration.objects.filter(email=check_email)
    data1 = account_registration.objects.filter(email=check_email).values_list('account_type').first()
    data2 = account_registration.objects.filter(email=check_email).values_list('account_complete').first()

    user_email.append(check_email)
    user_account_type.append(data2[0])

    if data1[0] == 'Applicant':
        if data2[0] == 'True':
            context = {'info': data}
            return render(request, 'html_files/User-Profile1.html', context)
        else: 
            context = {'info': data}
            return render(request, 'html_files/Finish-Registration.html', context)

    elif data1[0] == 'Employee':
        context = {'info': data}
        return render(request, 'html_files/Employee-Details.html', context)

    elif data1[0] == 'HRManager':
        data3 = account_registration.objects.all()
        #data4 = interview.objects.all()
        context = {'info': data3}
        return render(request, 'html_files/HRMANAGER.html', context)
    
def re_login(request):
    if request.method=='POST' and 'later' in request.POST:
        return redirect('user_profile')
    if request.method=='POST' and 'continue' in request.POST:
        return redirect ('signup1')

def signup(request):
    form = first_registration()
    if request.method == "POST":
        form = first_registration(request.POST, request.FILES)
        if form.is_valid():
            position = request.POST.get('job')
            form.instance.account_type = position
            form.save()
            return redirect ('signup')

    context = {'form':form}
    return render(request, 'html_files/Registration-Form.html', context)

def signup1(request):
    return render(request, 'html_files/Registration-Form-Part-2.html')

def complete_info(request):
    return render(request, 'html_files/Finish-Registration.html')

def user_profile(request):
    data = account_registration.objects.filter(email=user_email[0])
    context = {'info': data}
    return render(request, 'html_files/User-Profile1.html', context)


################################### INACTICVE ############################################

def change_pass(request):
    return render(request, 'html_files/changepassHR.html')

def hrdashboard(request):
    return render(request, 'html_files/HRMANAGER.html')

def delete(request):
    return render(request, 'html_files/delete.html')

def addjob(request):
    return render(request, 'html_files/Making-a-Job-Posting.html')

def profile(request):
    return render(request, 'html_files/User Profile.html')

def showAccount(request):
    return render(request,"html_files/User-Profile1.html")

def createJobs(request):
    return render(request, 'html_files/HRMANAGER.html')

def job_show(request):
    return render(request,"html_files/HOMEWEBSITE.html")

def changepass1(request):
    return render(request, 'html_files/HRMANAGER.html')

def delete_acc(request):
    return render(request, 'html_files/HRMANAGER.html')

def delete_jobs(request):
    return render(request, 'html_files/HRMANAGER.html')


################################### DEBUG ############################################

def home_debug(request):
    data = job_listing.objects.all()
    context = {'job': data}
    return render(request, 'html_files/HOMEWEBSITE-DEBUG.html', context)