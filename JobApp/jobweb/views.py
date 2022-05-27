from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

######################## WEBSITE ###########################


#request.is_authenticated
#request.usedr.account_typed
hr_account_login_email = []

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        data = account_registration.objects.filter(username=username)
        data1 = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()
 
        if user is not None:
            if data1 == 'Applicant Level 1':
                login(request, user)
                return redirect('applicant_level1', username=username)
            
            elif data1 == 'Applicant Level 2':
                login(request, user)
                return redirect('applicant_level_2_3_employee', username=username)
                
            elif data1 == 'Applicant Level 3':
                login(request, user)
                return redirect('applicant_level_2_3_employee', username=username)

            elif data1 == 'Employee':
                login(request, user)
                return redirect('applicant_level_2_3_employee', username=username)

            elif data1 == 'HRManager':
                login(request, user)
                hr_account_login_email.append(username)
                return redirect('hrdashboard', username=username)
            
            elif data1 == 'Rejected':
                login(request, user)
                return redirect('rejected_user', username=username)
       
            elif data1 == 'Retired':
                login(request, user)
                return redirect('retired_user', username=username)

            elif data1 == 'Terminate':
                login(request, user)
                return redirect('terminated_user', username=username)
            
            else:
                return redirect('home')
        
        else:
            return redirect('home')
    else:
        return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    hr_account_login_email.clear()
    return redirect('home')

def signup(request):
    form = first_registration()

    if request.method == "POST":
        form = first_registration(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password_first = form.cleaned_data.get("password1")
            password_confirm = form.cleaned_data.get("password2")

            first = form.cleaned_data.get('first_name')
            last = form.cleaned_data.get('last_name')
            middle = form.cleaned_data.get('middle_name')

            if password_confirm == password_first:
                position = request.POST.get('job')
                form.instance.account_type = position

                other_info.objects.create(username_id=username)
                interview.objects.create(username_id=username, first_name=first, middle_name=middle, last_name=last)

                form.save()

                messages.success(request, 'Account successfully created!')
                return redirect('home')

            else:
                messages.warning(request, 'ERROR: Password do not match.')
                return redirect('signup')
   
    context = {'form': form}
    return render(request, 'html_files/Registration-Form.html', context)

def signup1(request, username):
    
    if request.user.is_authenticated and request.user.account_type == "Applicant Level 1":
        profile = other_info.objects.get(username=username)
        form1 = second_registration(instance=profile)

        if request.method == "POST":
            form1 = second_registration(request.POST, request.FILES, instance=profile)
            
            if form1.is_valid():
                form1.save()
                #other_info.objects.filter(username_id=username).update(form1.save())
        
                account_registration.objects.filter(username=username).update(account_type='Applicant Level 2')
                info1 = account_registration.objects.filter(username=username)
                info2 = other_info.objects.filter(username=username)
                info3 = interview.objects.filter(username=username)

                messages.success(request, 'Registration Complete.')
                zippedItems = zip(info1, info2, info3)
                context1 = {'info': zippedItems}
                return render(request, 'html_files/User-Profile1.html', context1)

            else:
                return redirect('signup1')
            
        context = {'form': form1}
        return render(request, 'html_files/Registration-Form-Part-2.html', context)

    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

########################### APPLICANT//EMPLOYEE ###########################

@login_required(login_url='/login_user')
def user_profile(request, username):
    if request.user.is_authenticated and request.user.account_type == "Applicant Level 1" or request.user.is_authenticated and request.user.account_type == "Applicant Level 3" or request.user.is_authenticated and request.user.account_type == "Employee":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username_id=username)
        info3 = interview.objects.filter(username_id=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)

    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

@login_required(login_url='/login_user')
def returntoprofile(request, username):
    if request.user.is_authenticated and request.user.account_type == "Applicant Level 1" or request.user.is_authenticated and request.user.account_type == "Applicant Level 3" or request.user.is_authenticated and request.user.account_type == "Employee":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username_id=username)
        info3 = interview.objects.filter(username_id=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

@login_required(login_url='/login_user')
def requirements(request, username):
    if request.user.is_authenticated and request.user.account_type == "Applicant Level 1" or request.user.is_authenticated and request.user.account_type == "Applicant Level 2" or request.user.is_authenticated and request.user.account_type == "Applicant Level 3" or request.user.is_authenticated and request.user.account_type == "Employee":
        data1 = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()
        print('@@@@@@@@@@@@@')
        print(data1)

        if data1 == 'Applicant Level 1':
            messages.error(request, 'Please finish registration before submitting requirements.')
            return redirect('user_profile', username=username)

        else:
            data = other_info.objects.filter(username_id=username)
            context1 = {'check': data}
            return render(request, 'html_files/Requirements.html', context1)
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

@login_required(login_url='/login_user')
def requirements_satisfied(request, username_id):
    if request.user.is_authenticated and request.user.account_type == "Applicant Level 1" or request.user.is_authenticated and request.user.account_type == "Applicant Level 2" or request.user.is_authenticated and request.user.account_type == "Applicant Level 3" or request.user.is_authenticated and request.user.account_type == "Employee":
        if request.method == "POST":
            update_philhealth = request.POST.get('philhealth')
            update_pagibig = request.POST.get('pagibig')
            update_tin = request.POST.get('TIN')
            update_nbi = request.POST.get('NBI')
            update_sss = request.POST.get('SSS')
            update_medrecord = request.POST.get('medical')
            print('@@@@@@@@@@@@@@')
            print(update_philhealth, update_pagibig, update_tin, update_nbi, update_sss, update_medrecord)

            account_registration.objects.filter(username=username_id).update(account_type='Applicant Level 3')
            other_info.objects.filter(username_id=username_id).update(philhealth=update_philhealth, pagibig=update_pagibig, TIN=update_tin, NBI=update_nbi, SSS=update_sss, med_record=update_medrecord)

            info1 = account_registration.objects.filter(username=username_id)
            info2 = other_info.objects.filter(username_id=username_id)
            info3 = interview.objects.filter(username_id=username_id)
            
            messages.success(request, 'Requirements successfully submitted.')
            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1.html', context1)
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

########################### HR MANAGER ###########################

@login_required(login_url='/login_user')
def delete_account(request, username):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        account_registration.objects.filter(username=username).delete()
        interview.objects.filter(username=username).delete()
        other_info.objects.filter(username=username).delete()

        messages.success(request, 'Account successfully DELETED.')
        account = account_registration.objects.all()
        user_interview = interview.objects.values('date_time')
        hr_account = account_registration.objects.filter(username=username)
            
        zippedItems = zip(account, user_interview)
        return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})
        
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

@login_required(login_url='/login_user')
def manage_account(request, username):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        user_account = account_registration.objects.filter(username=username)
        data1 = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()

        if data1 == "Applicant Level 1":
            info1 = account_registration.objects.filter(username=username)
            info2 = other_info.objects.filter(username_id=username)
            info3 = interview.objects.filter(username_id=username)

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1-Applicant.html', context1)

        elif data1 == "Applicant Level 2":
            info1 = account_registration.objects.filter(username=username)
            info2 = other_info.objects.filter(username_id=username)
            info3 = interview.objects.filter(username_id=username)

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1-Applicant.html', context1)

        elif data1 == "Applicant Level 3":
            info1 = account_registration.objects.filter(username=username)
            info2 = other_info.objects.filter(username_id=username)
            info3 = interview.objects.filter(username_id=username)

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1-Applicant.html', context1)

        elif data1 == "Employee":
            info1 = account_registration.objects.filter(username=username)
            info2 = other_info.objects.filter(username_id=username)
            info3 = interview.objects.filter(username_id=username)

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1-Employee.html', context1)

        elif data1 == "Rejected":
            info1 = account_registration.objects.filter(username=username)
            info2 = other_info.objects.filter(username_id=username)
            info3 = interview.objects.filter(username_id=username)

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1-Applicant.html', context1)

        elif data1 == "Retired":
            info1 = account_registration.objects.filter(username=username)
            info2 = other_info.objects.filter(username_id=username)
            info3 = interview.objects.filter(username_id=username)

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1-Employee.html', context1)

        elif data1 == "Terminate":
            info1 = account_registration.objects.filter(username=username)
            info2 = other_info.objects.filter(username_id=username)
            info3 = interview.objects.filter(username_id=username)

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1-Applicant.html', context1)


   
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')
    
@login_required(login_url='/login_user')
def sort_list(request):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        if request.method == "POST" and "Name" in request.POST:
        
            account = account_registration.objects.order_by('first_name')
            user_interview = interview.objects.order_by('first_name')
            zippedItems = zip(account, user_interview)

            context1 = {'zippedItems': zippedItems}
            return render(request, 'html_files/HRMANAGER.html', context1)
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

@login_required(login_url='/login_user')
def set_interview(request, username_id):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        get_date_time = request.POST.get('interview_date')
        
        if get_date_time != "":
            if request.method == "POST":
                update_date_time = interview.objects.get(username=username_id)
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
            user_account = account_registration.objects.filter(username=username_id)
            context = {'info': user_account}
            return render(request, 'html_files/User-Profile1-Applicant.html', context)
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

@login_required(login_url='/login_user')
def change_employment(request, username):
    if request.user.is_authenticated and request.user.account_type == "HRManager":

        if request.method == "POST" and "Full Time" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Full Time Worker")
            messages.success(request, 'Employment was updated on account: ' + username)

            account = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            hr_account = account_registration.objects.filter(username=username)

            zippedItems = zip(account, user_interview)
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})

        elif request.method == "POST" and "Part Time" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Part Time Worker")
            messages.success(request, 'Employment was updated on account: ' + username)
            account = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            hr_account = account_registration.objects.filter(username=username)
            
            zippedItems = zip(account, user_interview)
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})

        elif request.method == "POST" and "On Leave" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="On Vacation")
            messages.success(request, 'Employment was updated on account: ' + username)
            account = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            hr_account = account_registration.objects.filter(username=username)
            
            zippedItems = zip(account, user_interview)
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})

        elif request.method == "POST" and "Resigned" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Resigned")
            messages.success(request, 'Employment was updated on account: ' + username)
            aaccount = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            hr_account = account_registration.objects.filter(username=username)
            
            zippedItems = zip(account, user_interview)
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})

        elif request.method == "POST" and "Fired" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Fired")
            messages.success(request, 'Employment was updated on account: ' + username)
            account = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            hr_account = account_registration.objects.filter(username=username)
            
            zippedItems = zip(account, user_interview)
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})

        elif request.method == "POST" and "Retired" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Retired")
            account_registration.objects.filter(username=username).update(account_type="Retired")
            account_registration.objects.filter(username=username).update(applyingfor="Retired")

            messages.success(request, 'Employment was updated on account: ' + username)
            account = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            hr_account = account_registration.objects.filter(username=username)
            
            zippedItems = zip(account, user_interview)
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})

        elif request.method == "POST" and "Terminate" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Terminate")
            account_registration.objects.filter(username=username).update(account_type="Terminate")
            account_registration.objects.filter(username=username).update(applyingfor="Terminate")

            messages.success(request, 'Employment was Terminated.' + username)
            account = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            hr_account = account_registration.objects.filter(username=username)
            
            zippedItems = zip(account, user_interview)
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})
            
        elif request.method == "POST" and "Promoted" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="HRManager")
            account_registration.objects.filter(username=username).update(account_type="HRManager")
            account_registration.objects.filter(username=username).update(applyingfor="HRManager")

            messages.success(request, 'Employment Account was Promoted.' + username)
            account = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            hr_account = account_registration.objects.filter(username=username)
            
            zippedItems = zip(account, user_interview)
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})

            Promoted

        else:
            return redirect('change_employment')
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

@login_required(login_url='/login_user')
def applicant_hired_reject(request, username):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        check_type = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()

        if request.method == "POST" and "Hire" in request.POST:
            if check_type == 'Applicant Level 1':
                messages.error(request, 'Applicant not fully registered.')
                return redirect('manage_account', username=username)

            elif check_type == 'Applicant Level 2':
                messages.error(request, 'Applicant not submitted requirements.')
                return redirect('manage_account', username=username)

            elif check_type == 'Applicant Level 3':
                update_job = account_registration.objects.filter(username=username).values_list('applyingfor', flat=True).first()

                account_registration.objects.filter(username=username).update(job=update_job)

                account_registration.objects.filter(username=username).update(applyingfor='')

                account_registration.objects.filter(username=username).update(account_type="Employee")
                interview.objects.filter(username=username).update(date_time=None)
                messages.success(request, 'Applicant Successfully Hired!')


                account = account_registration.objects.all()
                user_interview = interview.objects.values('date_time')
                hr_account = account_registration.objects.filter(username=username)

                zippedItems = zip(account, user_interview)
                context1 = {'zippedItems': zippedItems}
                context2 = {'hr_account': hr_account}
                return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})

        if request.method == "POST" and "Reject" in request.POST:
            account_registration.objects.filter(username=username).update(account_type="Rejected")

            messages.success(request, 'Applicant succesfully Rejected.')
            account = account_registration.objects.all()
            user_interview = interview.objects.values('date_time')
            hr_account = account_registration.objects.filter(username=username)

            zippedItems = zip(account, user_interview)
            context1 = {'zippedItems': zippedItems}
            context2 = {'hr_account': hr_account}
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

########################### GENERAL ###########################

@login_required(login_url='/login_user')
def change_password(request, username):
    form = update_password()
    
    if request.method == "POST":
        form = update_password(request.POST)

        if form.is_valid():
            new_pass = request.POST.get('password1')
            form = account_registration.objects.get(username=username)
            form.set_password(new_pass)
            form.save()

            info1 = account_registration.objects.filter(username=username)
            info2 = other_info.objects.filter(username_id=username)
            info3 = interview.objects.filter(username_id=username)

            check_type = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()
            
            if check_type == 'HRManager':
                account = account_registration.objects.all()
                user_interview = interview.objects.values('date_time')
                hr_account = account_registration.objects.filter(username=username)
                messages.success(request, 'Password changed successfully.')
                zippedItems = zip(account, user_interview)
                context1 = {'zippedItems': zippedItems}
                return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})

            else:
                messages.success(request, 'Password changed successfully.')
                zippedItems = zip(info1, info2, info3)
                context1 = {'info': zippedItems}
                return render(request, 'html_files/User-Profile1.html', context1)

        else:
            return redirect('change_password', username=username)

    context = {'form': form }
    return render(request, 'html_files/Changepassword.html', context)

@login_required(login_url='/login_user')
def add_job(request, username):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        user = account_registration.objects.filter(username=username)
        context = {'user' : user}
        return render(request, 'html_files/Making-a-Job-Posting.html', context)
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')



################################### REDIRECTS ############################################
def home(request):
    asd = job_listing.objects.all()
    context = { 'job' : asd }
    return render(request, 'html_files/HOMEWEBSITE.html', context)

@login_required(login_url='/login_user')
def hrdashboard(request, username):
    
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        account = account_registration.objects.all()
        user_interview = interview.objects.values('date_time')
        hr_account = account_registration.objects.filter(username=username)

        zippedItems = zip(account, user_interview)
        context1 = {'zippedItems': zippedItems}
        context2 = {'hr_account': hr_account}
        return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

@login_required(login_url='/login_user')
def applicant_level1(request, username):

    if request.user.is_authenticated and request.user.account_type == "Applicant Level 1":
        data = account_registration.objects.filter(username=username)
        context = {'info': data}
        return render(request, 'html_files/Finish-Registration.html', context)
            
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

def applicant_level_2_3_employee(request, username):
    if request.user.is_authenticated and request.user.account_type == "Applicant Level 2" or request.user.is_authenticated and request.user.account_type == "Applicant Level 3" or request.user.is_authenticated and request.user.account_type == "Employee":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username=username)
        info3 = interview.objects.filter(username=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)

    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

def rejected_user(request, username):
    if request.user.is_authenticated and request.user.account_type == "Rejected":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username=username)
        info3 = interview.objects.filter(username=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)
        
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

def retired_user(request, username):
    if request.user.is_authenticated and request.user.account_type == "Retired":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username=username)
        info3 = interview.objects.filter(username=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)
        
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

def terminated_user(request, username):
    if request.user.is_authenticated and request.user.account_type == "Terminate":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username=username)
        info3 = interview.objects.filter(username=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)
        
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

################################### In progress ############################################
def list_job(request,username):
    print('TEST @@@@@@@@')
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        print('TEST 1')
        if request.method == "POST":
            print('TEST 2')
            job_title = request.POST['job_title']
            job_desc = request.POST['job_description']
            job_req = request.POST['jobreq1']
            job_req2 = request.POST['jobreq2']
            work_pay = request.POST['salary']
            print('TEST 3')

            job_listing.objects.create(jtitle=job_title, jdesc=job_desc, jobreq1=job_req, jobreq2=job_req2, salary=work_pay)

            print('TEST 4')
            messages.success(request, 'Job is ADDED successfully.')
            return redirect('hrdashboard', username=username)
            

    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

def delete_job(request, username):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        if request.method == "POST":

            job_name = request.POST['deletejob']
            job1 = job_listing.objects.filter(jtitle=job_name).values_list('jtitle', flat=True).first()
            print(job1)
            if job_name == job1:
                job_listing.objects.filter(jtitle=job_name).delete()

                messages.success(request, 'Job is DELETED succesfully.')
                return redirect('hrdashboard', username=username)
            
            else:
                messages.warning(request, 'No Job Title was found.')
                return redirect('add_job', username=username)
    else:
        hr_account_login_email.clear()
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('home')

################################### DEBUG ############################################


