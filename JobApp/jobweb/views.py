from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
################################################ WEBSITE ######################################################

#hr_account_login_email = []
#login_authorization = []

def home(request):
    asd = job_listing.objects.all()
    context = { 'job' : asd }
    return render(request, 'html_files/HOMEWEBSITE.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        data = account_registration.objects.filter(username=username)
        data1 = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()
        data2 = account_registration.objects.filter(username=username).values_list('verified_user', flat=True).first()
 
        if user is not None:
            if data1 == 'Applicant Level 1':
                login(request, user)
                messages.info(request, 'Log in successful.')
                return redirect('applicant_level1', username=username)
            
            elif data1 == 'Applicant Level 2':
                login(request, user)
                messages.info(request, 'Log in successful.')
                return redirect('applicant_level_2_3_employee', username=username, verified_user=data2)
                
            elif data1 == 'Applicant Level 3':
                login(request, user)
                messages.info(request, 'Log in successful.')
                return redirect('applicant_level_2_3_employee', username=username, verified_user=data2)

            elif data1 == 'Employee':
                login(request, user)
                messages.info(request, 'Log in successful.')
                return redirect('applicant_level_2_3_employee', username=username, verified_user=data2)

            elif data1 == 'HRManager':
                login(request, user)
                messages.info(request, 'Log in successful.')
                return redirect('hrdashboard', username=username, verified_user=data2)
            
            elif data1 == 'Rejected':
                login(request, user)
                messages.info(request, 'Log in successful.')
                return redirect('rejected_user', username=username)
       
            elif data1 == 'Retired':
                login(request, user)
                messages.info(request, 'Log in successful.')
                return redirect('retired_user', username=username)

            elif data1 == 'Terminate':
                login(request, user)
                messages.info(request, 'Log in successful.')
                return redirect('terminated_user', username=username)
            
            else:
                messages.info(request, 'Account does not have any account type, Please set an account type in database')
                return redirect('home')
        else:
            messages.info(request, 'Email or Password is incorrect, please try again.')
            return redirect('home')
    else:
        return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
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

def signup1(request, username, verified_user):
    if request.user.is_authenticated and request.user.account_type == "Applicant Level 1" and request.user.verified_user == False:
        profile = other_info.objects.get(username=username)
        form1 = second_registration(instance=profile)

        if request.method == "POST":
            form1 = second_registration(request.POST, request.FILES, instance=profile)
            
            if form1.is_valid():
                form1.save()
        
                account_registration.objects.filter(username=username).update(account_type='Applicant Level 2')
                account_registration.objects.filter(username=username).update(verified_user=True)
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
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

########################### APPLICANT//EMPLOYEE ###########################

@login_required(login_url='/login_user')
def user_profile(request, username, verified_user):
    if request.user.verified_user == False and request.user.is_authenticated and request.user.account_type == "Applicant Level 1" or request.user.is_authenticated and request.user.account_type == "Applicant Level 3" or request.user.is_authenticated and request.user.account_type == "Employee":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username_id=username)
        info3 = interview.objects.filter(username_id=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)

    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

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
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def rejected_user(request, username):
    if request.user.username==username and request.user.is_authenticated and request.user.account_type == "Rejected":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username=username)
        info3 = interview.objects.filter(username=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)
        
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def retired_user(request, username):
    if request.user.username==username and request.user.is_authenticated and request.user.account_type == "Retired":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username=username)
        info3 = interview.objects.filter(username=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)
        
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def terminated_user(request, username):
    if request.user.username==username and request.user.is_authenticated and request.user.account_type == "Terminate":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username=username)
        info3 = interview.objects.filter(username=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)
        
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def requirements(request, username, verified_user):
    if request.user.verified_user == False and request.user.is_authenticated and request.user.account_type == "Applicant Level 1" or request.user.is_authenticated and request.user.account_type == "Applicant Level 2" or request.user.is_authenticated and request.user.account_type == "Applicant Level 3" or request.user.is_authenticated and request.user.account_type == "Employee":
        data1 = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()

        if data1 == 'Applicant Level 1':
            messages.error(request, 'Please finish registration before submitting requirements.')
            return redirect('user_profile', username=username, verified_user=verified_user)

        else:
            data = other_info.objects.filter(username_id=username)
            context1 = {'check': data}
            return render(request, 'html_files/Requirements.html', context1)
            
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def requirements_satisfied(request, username_id):
    if request.user.username==username_id and request.user.is_authenticated and request.user.account_type == "Applicant Level 1" or request.user.username==username_id and request.user.is_authenticated and request.user.account_type == "Applicant Level 2" or request.user.username==username_id and request.user.is_authenticated and request.user.account_type == "Applicant Level 3" or request.user.username==username_id and request.user.is_authenticated and request.user.account_type == "Employee":
        if request.method == "POST":
            update_philhealth = request.POST.get('philhealth')
            update_pagibig = request.POST.get('pagibig')
            update_tin = request.POST.get('TIN')
            update_nbi = request.POST.get('NBI')
            update_sss = request.POST.get('SSS')
            update_medrecord = request.POST.get('medical')

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
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def applicant_level1(request, username):
    if request.user.is_authenticated and request.user.account_type == "Applicant Level 1" and request.user.verified_user == False:
        data = account_registration.objects.filter(username=username)
        context = {'info': data}
        return render(request, 'html_files/Finish-Registration.html', context)
            
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def applicant_level_2_3_employee(request, username, verified_user):
    if request.user.verified_user == True and request.user.is_authenticated and request.user.account_type == "Applicant Level 2" or request.user.verified_user == True and request.user.is_authenticated and request.user.account_type == "Applicant Level 3" or request.user.verified_user == True and request.user.verified_user == True and request.user.is_authenticated and request.user.account_type == "Employee":
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username=username)
        info3 = interview.objects.filter(username=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)

    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')


###################################################### HR MANAGER ######################################################


@login_required(login_url='/login_user')
def hrdashboard(request, username, verified_user):
    if request.user.verified_user == True and request.user.is_authenticated and request.user.account_type == "HRManager":
        account = account_registration.objects.all()
        user_interview = interview.objects.values('date_time')
        hr_account = account_registration.objects.filter(username=request.user.username)

        zippedItems = zip(account, user_interview)
        return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})
            
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def delete_account(request, username, verified_user):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        data2 = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()

        if data2 == 'Applicant Level 1':
            account_registration.objects.filter(username=username).delete()
            interview.objects.filter(username=username).delete()
            other_info.objects.filter(username=username).delete()
            messages.success(request, 'Account succesfully Deleted.')

            send_mail(
                        'Account Deleted.', #SUBJECT
                        'We would like you inform you that your account has been deleted from our website Job Web App, thank you for understanding', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif data2 == 'Applicant Level 2':
            account_registration.objects.filter(username=username).delete()
            interview.objects.filter(username=username).delete()
            other_info.objects.filter(username=username).delete()
            messages.success(request, 'Account succesfully Deleted.')

            send_mail(
                        'Account Deleted.', #SUBJECT
                        'We would like you inform you that your account has been deleted from our website Job Web App, thank you for understanding', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif data2 == 'Applicant Level 3':
            account_registration.objects.filter(username=username).delete()
            interview.objects.filter(username=username).delete()
            other_info.objects.filter(username=username).delete()
            messages.success(request, 'Account succesfully Deleted.')

            send_mail(
                        'Account Deleted.', #SUBJECT
                        'We would like you inform you that your account has been deleted from our website Job Web App, thank you for understanding', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif data2 == 'Employee':
            account_registration.objects.filter(username=username).delete()
            interview.objects.filter(username=username).delete()
            other_info.objects.filter(username=username).delete()
            messages.success(request, 'Account succesfully Deleted.')

            send_mail(
                        'Account Deleted.', #SUBJECT
                        'We would like you inform you that your account has been deleted from our website Job Web App, thank you for understanding', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif data2 == 'Terminate':
            account_registration.objects.filter(username=username).delete()
            interview.objects.filter(username=username).delete()
            other_info.objects.filter(username=username).delete()
            messages.success(request, 'Account succesfully Deleted.')

            send_mail(
                        'Account Deleted.', #SUBJECT
                        'We would like you inform you that your account has been deleted from our website Job Web App, thank you for understanding', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif data2 == 'Retired':
            account_registration.objects.filter(username=username).delete()
            interview.objects.filter(username=username).delete()
            other_info.objects.filter(username=username).delete()
            messages.success(request, 'Account succesfully Deleted.')

            send_mail(
                        'Account Deleted.', #SUBJECT
                        'We would like you inform you that your account has been deleted from our website Job Web App, thank you for understanding', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif data2 == 'Rejected':
            account_registration.objects.filter(username=username).delete()
            interview.objects.filter(username=username).delete()
            other_info.objects.filter(username=username).delete()
            messages.success(request, 'Account succesfully Deleted.')

            send_mail(
                        'Account Deleted.', #SUBJECT
                        'We would like you inform you that your account has been deleted from our website Job Web App, thank you for understanding', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        else:
            account_registration.objects.filter(username=username).delete()
            interview.objects.filter(username=username).delete()
            other_info.objects.filter(username=username).delete()
            messages.success(request, 'Account succesfully Deleted.')
            return redirect('hrdashboard', username=request.user.username, verified_user=verified_user)
       
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def manage_account(request, username, verified_user):
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
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')
    
@login_required(login_url='/login_user')
def sort_list(request):
    if request.user.verified_user == True and request.user.is_authenticated and request.user.account_type == "HRManager":
        if request.method == "POST" and "Name" in request.POST:
        
            account = account_registration.objects.order_by('first_name')
            user_interview = interview.objects.order_by('first_name')
    
            hr_account = account_registration.objects.filter(username=request.user.username)
            zippedItems = zip(account, user_interview)
            return render(request, 'html_files/HRMANAGER.html', {'zippedItems': zippedItems, 'hr_account': hr_account})
            
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def set_interview(request, username_id, verified_user):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        get_date_time = request.POST.get('interview_date')
        data2 = account_registration.objects.filter(username=username_id).values_list('account_type', flat=True).first()
        
        if get_date_time == "":
            messages.success(request, 'Please set a time and date.')
            info1 = account_registration.objects.filter(username=username_id)
            info2 = other_info.objects.filter(username_id=username_id)
            info3 = interview.objects.filter(username_id=username_id)

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1-Applicant.html', context1)
                    
        else:
            if request.method == "POST":
                if data2 == 'Applicant Level 1':
                    update_date_time = interview.objects.get(username=username_id)
                    update_date_time.date_time = get_date_time
                    update_date_time.save()

                    send_mail(
                        'Interview', #SUBJECT
                        'Your interview date was updated to: ' + get_date_time, #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username_id], #TO
                    )

                    messages.success(request, 'Interview date was added.')
                    return redirect('hrdashboard', username=request.user.username, verified_user=True)

                elif data2 == 'Applicant Level 2':
                    update_date_time = interview.objects.get(username=username_id)
                    update_date_time.date_time = get_date_time
                    update_date_time.save()

                    send_mail(
                        'Interview', #SUBJECT
                        'Your interview date was updated.' + get_date_time, #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username_id], #TO
                    )

                    messages.success(request, 'Interview date was added.')
                    return redirect('hrdashboard', username=request.user.username, verified_user=True)

                elif data2 == 'Applicant Level 3':
                    update_date_time = interview.objects.get(username=username_id)
                    update_date_time.date_time = get_date_time
                    update_date_time.save()

                    send_mail(
                        'Interview', #SUBJECT
                        'Your interview date was updated.' + get_date_time, #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username_id], #TO
                    )

                    messages.success(request, 'Interview date was added.')
                    return redirect('hrdashboard', username=request.user.username, verified_user=True)

                else:
                    update_date_time = interview.objects.get(username=username_id)
                    update_date_time.date_time = get_date_time
                    update_date_time.save()

                    messages.success(request, 'Interview date was added.')
                    return redirect('hrdashboard', username=request.user.username, verified_user=verified_user)

    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def change_employment(request, username, verified_user):
    if request.user.is_authenticated and request.user.account_type == "HRManager":

        if request.method == "POST" and "Full Time" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Full Time Worker")
            messages.success(request, 'Employment was updated on account: ' + username)

            send_mail(
                        'Employment Updated', #SUBJECT
                        'Your employment was updated successfully to FULL TIME', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif request.method == "POST" and "Part Time" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Part Time Worker")
            messages.success(request, 'Employment was updated on account: ' + username)

            send_mail(
                        'Employment Updated', #SUBJECT
                        'Your employment was updated successfully to PART TIME', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif request.method == "POST" and "On Leave" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="On Vacation")
            messages.success(request, 'Employment was updated on account: ' + username)

            send_mail(
                        'Employment Updated', #SUBJECT
                        'Your employment was updated successfully to ON LEAVE', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif request.method == "POST" and "Resigned" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Resigned")
            messages.success(request, 'Employment was updated on account: ' + username)

            send_mail(
                        'Employment Updated', #SUBJECT
                        'Your employment was updated successfully to RESIGNED', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif request.method == "POST" and "Retired" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Retired")
            account_registration.objects.filter(username=username).update(account_type="Retired")
            account_registration.objects.filter(username=username).update(applyingfor="Retired")

            send_mail(
                        'Employment Updated', #SUBJECT
                        'Your employment was updated successfully to RETIRED', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )


            messages.success(request, 'Employment was updated on account: ' + username)

            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        elif request.method == "POST" and "Terminate" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="Terminate")
            account_registration.objects.filter(username=username).update(account_type="Terminate")
            account_registration.objects.filter(username=username).update(applyingfor="Terminate")

            send_mail(
                        'Employment Updated', #SUBJECT
                        'Your account was terminated.', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            messages.success(request, 'Employment was Terminated.' + username)

            return redirect('hrdashboard', username=request.user.username, verified_user=True)
            
        elif request.method == "POST" and "Promoted" in request.POST:
            account_registration.objects.filter(username=username).update(employment_status="HRManager")
            account_registration.objects.filter(username=username).update(account_type="HRManager")
            account_registration.objects.filter(username=username).update(applyingfor="HRManager")

            send_mail(
                        'Employment Updated', #SUBJECT
                        'You have been promoted to be a HR Manager in the web app', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

            messages.success(request, 'Employment Account was Promoted.' + username)
            return redirect('hrdashboard', username=request.user.username, verified_user=True)

        else:
            return redirect('change_employment')
            
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def applicant_hired_reject(request, username, verified_user):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        check_type = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()

        if request.method == "POST" and "Hire" in request.POST:
            if check_type == 'Applicant Level 1':
                messages.error(request, 'Applicant not fully registered.')
                
                return redirect('manage_account', username=username, verified_user=verified_user)

            elif check_type == 'Applicant Level 2':
                messages.error(request, 'Applicant not submitted requirements.')
                return redirect('manage_account', username=username, verified_user=verified_user)

            elif check_type == 'Applicant Level 3':

                send_mail(
                        'HIRED!!!', #SUBJECT
                        'You are now Hired in the Company', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

                update_job = account_registration.objects.filter(username=username).values_list('applyingfor', flat=True).first()
                account_registration.objects.filter(username=username).update(job=update_job)
                account_registration.objects.filter(username=username).update(applyingfor='')
                account_registration.objects.filter(username=username).update(account_type="Employee")
                interview.objects.filter(username=username).update(date_time=None)
                
                messages.success(request, 'Applicant Successfully Hired!')

                return redirect('hrdashboard', username=request.user.username, verified_user=True)

        if request.method == "POST" and "Reject" in request.POST:
            data2 = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()
            print(data2)

            if data2 == 'Applicant Level 1':

                send_mail(
                        'Application Rejected', #SUBJECT
                        'Thank you for applying at our website.', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

                account_registration.objects.filter(username=username).update(account_type="Rejected")
                account_registration.objects.filter(username=username).update(applyingfor="")
                messages.success(request, 'Applicant succesfully Rejected.')
                return redirect('hrdashboard', username=request.user.username, verified_user=True)

            elif data2 == 'Applicant Level 2':

                send_mail(
                        'Application Rejected', #SUBJECT
                        'Thank you for applying at our website.', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

                account_registration.objects.filter(username=username).update(account_type="Rejected")
                account_registration.objects.filter(username=username).update(applyingfor="")
                messages.success(request, 'Applicant succesfully Rejected.')
                return redirect('hrdashboard', username=request.user.username, verified_user=True)

            elif data2 == 'Applicant Level 3':

                send_mail(
                        'Application Rejected', #SUBJECT
                        'Thank you for applying at our website.', #MESSAGE
                        'appjobweb@gmail.com', #FROM
                        [username], #TO
                    )

                account_registration.objects.filter(username=username).update(account_type="Rejected")
                account_registration.objects.filter(username=username).update(applyingfor="")
                messages.success(request, 'Applicant succesfully Rejected.')
                return redirect('hrdashboard', username=request.user.username, verified_user=verified_user)

            else:      
                account_registration.objects.filter(username=username).update(account_type="Rejected")
                account_registration.objects.filter(username=username).update(applyingfor="")
                messages.success(request, 'Applicant succesfully Rejected.')
                return redirect('hrdashboard', username=request.user.username, verified_user=verified_user)
            
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def manage_joblisting(request, username, verified_user):
    if request.user.username==username and request.user.is_authenticated and request.user.account_type == "HRManager":
        user = account_registration.objects.filter(username=username)
        context = {'user' : user}
        return render(request, 'html_files/Making-a-Job-Posting.html', context)
            
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def list_job(request, username, verified_user):
    if request.user.verified_user == True and request.user.is_authenticated and request.user.account_type == "HRManager":
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
            return redirect('hrdashboard', username=username, verified_user=verified_user)

    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page.account_registrationuopda Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def delete_job(request, username, verified_user):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        if request.method == "POST":

            job_name = request.POST['deletejob']
            job1 = job_listing.objects.filter(jtitle=job_name).values_list('jtitle', flat=True).first()
            print(job1)
            if job_name == job1:
                job_listing.objects.filter(jtitle=job_name).delete()
                messages.success(request, 'Job is DELETED succesfully.')
                return redirect('hrdashboard', username=username, verified_user=verified_user)
            
            else:
                messages.warning(request, 'No Job Title was found.')
                return redirect('manage_joblisting', username=username, verified_user=verified_user)
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')


###################################################### GENERAL ######################################################

@login_required(login_url='/login_user')
def email_notify(request, username):
    if request.user.is_authenticated and request.user.account_type == "HRManager":
        send_mail(
                'Finish account now', #SUBJECT
                'We would like you inform you that we are now hiring you, but your account is not fully registered or did not pas requirements yet, please work up to Level 3 in order to Hire.', #MESSAGE
                'appjobweb@gmail.com', #FROM
                [username], #TO
            )
        
        info1 = account_registration.objects.filter(username=username)
        info2 = other_info.objects.filter(username_id=username)
        info3 = interview.objects.filter(username_id=username)

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1-Applicant.html', context1)
        
    else:
        messages.warning(request, 'You have been logged out because of accessing unauthorized page. Please log in again.')
        return redirect('logout_user')

@login_required(login_url='/login_user')
def change_password(request, username, verified_user):
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

################################### In progress ############################################

def applicant_employee_create_pdf(request, username, *args, **kwargs):
    account = get_object_or_404(account_registration, pk=username)
    second_info = get_object_or_404(other_info, pk=username)

    template_path = 'html_files/PDFViewer.html'
    context = {'account': account, 'second_info': second_info}
 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="RESUME.pdf"'
  
    template = get_template(template_path)
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



################################### DEBUG ############################################