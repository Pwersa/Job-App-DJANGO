import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
import mysql.connector
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import first_registration

def home(request):
    return render(request,"html_files/HOMEWEBSITE.html")

def completeInfo(request):
    return render(request, 'html_files/Registration-Form-Part-2.html')

def signup(request):
    form = first_registration()
    if request.method == "POST":
        form = first_registration(request.POST)
        if form.is_valid():
            position = request.POST.get('job')
            form.instance.account_type = position
            form.save()
            return redirect ('signup')

    context = {'form':form}
    return render(request, 'html_files/Registration-Form.html', context)

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
    return render(request,"html_files/User-Profile.html")

def createJobs(request):
    return render(request, 'html_files/HRMANAGER.html')

def job_show(request):
    return render(request,"html_files/HOMEWEBSITE.html")

def login(request):
    return render(request, 'html_files/HOMEWEBSITE.html')

def changepass1(request):
    return render(request, 'html_files/HRMANAGER.html')

def delete_acc(request):
    return render(request, 'html_files/HRMANAGER.html')

def delete_jobs(request):
    return render(request, 'html_files/HRMANAGER.html')