#from django.http import HttpResponse
#import mysql.connector
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
        context = {'account': data3}
        return render(request, 'html_files/HRMANAGER.html', context)
    
def re_login(request):
    if request.method =='POST' and 'later' in request.POST:
        return redirect('user_profile')
    if request.method =='POST' and 'continue' in request.POST:
        return redirect ('signup1')

def signup(request):
    form = first_registration()

    if request.method == "POST":
        form = first_registration(request.POST, request.FILES)

        if form.is_valid():
            password_first = form.cleaned_data.get("password1")
            password_confirm = form.cleaned_data.get("password2")

            if password_confirm == password_first:
                position = request.POST.get('job')
                form.instance.account_type = position
                form.save()
                messages.success(request, 'Account successfully created!')
                return redirect('home')

            else:
                messages.warning(request, 'ERROR: Password do not match.')
                return redirect('signup')

    context = {'form': form}
    return render(request, 'html_files/Registration-Form.html', context)

def hrdashboard(request):
    account = account_registration.objects.all()
    context = {'account': account}
    return render(request, 'html_files/HRMANAGER.html', context)

def sort_list(request):
    if request.method == "POST" and "Name" in request.POST:
        account = account_registration.objects.order_by('first_name')
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Emp_App" in request.POST:
        account = account_registration.objects.order_by('account_type')
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)
    
    elif request.method == "POST" and "Date" in request.POST:
        account = account_registration.objects.order_by('interview')
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    else:
        return redirect('sort_list')

def manage_account(request):
    print("MANAGE")
    account_email = request.POST['email']
    account_email_type = request.POST['account_type']

    if request.method == "POST" and 'Delete' in request.POST:
        account_registration.objects.filter(email=account_email).delete()
        print("DELETE")
        return redirect('hrdashboard')

    elif request.method == "POST" and 'View Account' in request.POST:

        if account_email_type == "Applicant":
            account_view = account_registration.objects.filter(email=account_email)
            context = {'info': account_view}
            print("VIEW Applicant")
            return render(request, 'html_files/User-Profile1-Applicant.html', context)

        elif account_email_type == "Employee":
            account_view = account_registration.objects.filter(email=account_email)
            context = {'info': account_view}
            print("VIEW Employee")
            return render(request, 'html_files/User-Profile1-Employee.html', context)

        else:
            return redirect('hrdashboard')

def signup1(request):
    return render(request, 'html_files/Registration-Form-Part-2.html')

def complete_info(request):
    return render(request, 'html_files/Finish-Registration.html')

def user_profile(request):
    data = account_registration.objects.filter(email=user_email[0])
    context = {'info': data}
    return render(request, 'html_files/User-Profile1.html', context)

def set_interview(request):
    return redirect('set_interview')

def change_employment(request):
    email = request.POST.get('account_email')

    if request.method == "POST" and "Full Time" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Full Time Worker")
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Part Time" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Part Time Worker")
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "On Leave" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="On Vacation")
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Resigned" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Resigned")
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Fired" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Fired")
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Retired" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Retired")
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    else:
        return redirect('change_employment')



################################### INACTIVE ############################################

def change_pass(request):
    return render(request, 'html_files/changepassHR.html')

def delete(request):
    return render(request, 'html_files/delete.html')

def addjob(request):
    return render(request, 'html_files/Making-a-Job-Posting.html')


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

def logout(request):
    logout()
    return redirect('home')


################################### DEBUG ############################################



 




