#from django.http import HttpResponse
#import mysql.connector
#from django.contrib.auth.forms import UserCreationForm
from queue import Empty
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


######################## ACTIVE #########################

def login(request):
    check_email = request.POST.get('email1')
    data = account_registration.objects.filter(email=check_email)
    data1 = account_registration.objects.filter(email=check_email).values_list('account_type', flat=True).first()
    #data2 = account_registration.objects.filter(email=check_email).values_list('account_complete', flat=True).first()

    print("data1" , data)
    print(data1)
    #print(data2)
    
    if data1 == 'Applicant Level 1':
        context = {'info': data}
        return render(request, 'html_files/Finish-Registration.html', context)
    
    elif data1 == 'Applicant Level 2':
        context = {'info': data}
        return render(request, 'html_files/Finish-Registration.html', context)

    elif data1 == 'Applicant Level 3':
        context = {'info': data}
        return render(request, 'html_files/Finish-Registration.html', context)

    elif data1 == 'Employee':
        context = {'info': data}
        return render(request, 'html_files/Employee-Details.html', context)

    elif data1 == 'HRManager':
        data3 = account_registration.objects.all()
        #data4 = interview.objects.all()
        context = {'account': data3}
        return render(request, 'html_files/HRMANAGER.html', context)
    
    else:
        return redirect('home')
    
def re_login(request, email):
    user_account = account_registration.objects.filter(email=email)
    context = {'info': user_account}
    return render(request, 'html_files/User-Profile1.html', context)

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

def manage_account(request, email):
    user_account = account_registration.objects.filter(email=email)
    data1 = account_registration.objects.filter(email=email).values_list('account_type', flat=True).first()

    if data1 == "Applicant Level 1":
        context = {'info': user_account}
        return render(request, 'html_files/User-Profile1-Applicant.html', context)

    elif data1 == "Applicant Level 2":
        context = {'info': user_account}
        return render(request, 'html_files/User-Profile1-Applicant.html', context)

    elif data1 == "Employee":
        context = {'info': user_account}
        return render(request, 'html_files/User-Profile1-Employee.html', context)

    elif data1 == "HRManager":  
        return redirect('hrdashboard')

def signup1(request):
    return render(request, 'html_files/Registration-Form-Part-2.html')

def complete_info(request):
    return render(request, 'html_files/Finish-Registration.html')


def set_interview(request, email_id):

    get_date_time = request.POST.get('interview_date')
    
    if get_date_time is not "":
        if request.method == "POST":
            update_date_time = interview.objects.get(email_id=email_id)
            update_date_time.date_time = get_date_time
            update_date_time.save()
            print("SET DATE:", get_date_time )

            account = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            zippedItems = zip(account, user_interview)

            messages.success(request, 'Interview date was added.')
            context1 = {'zippedItems': zippedItems}
            return render(request, 'html_files/HRMANAGER.html', context1)
            
    else:
        messages.success(request, 'No interview date was added.')
        user_account = account_registration.objects.filter(email=email_id)
        context = {'info': user_account}
        return render(request, 'html_files/User-Profile1-Applicant.html', context)

def change_employment(request, email):

    if request.method == "POST" and "Full Time" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Full Time Worker")
        messages.success(request, 'Employment was updated on account: ' + email)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Part Time" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Part Time Worker")
        messages.success(request, 'Employment was updated on account: ' + email)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "On Leave" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="On Vacation")
        messages.success(request, 'Employment was updated on account: ' + email)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Resigned" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Resigned")
        messages.success(request, 'Employment was updated on account: ' + email)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Fired" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Fired")
        messages.success(request, 'Employment was updated on account: ' + email)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Retired" in request.POST:
        account_registration.objects.filter(email=email).update(employment_status="Retired")
        messages.success(request, 'Employment was updated on account: ' + email)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    else:
        return redirect('change_employment')

################################### REDIRECTS ############################################

def home(request):
    data = job_listing.objects.all()
    context = {'job': data}
    return render(request, 'html_files/HOMEWEBSITE.html', context)

def hrdashboard(request):
    account = account_registration.objects.all()
    context = {'account': account}
    return render(request, 'html_files/HRMANAGER.html', context)

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


def applicant_hired_reject(request, email):
    if request.method == "POST" and "Hire" in request.POST:
        account_registration.objects.filter(email=email).update(account_type="Employee")
        messages.success(request, 'Applicant Successfully Hired!')
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)
