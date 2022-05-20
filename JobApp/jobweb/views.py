from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

######################## ACTIVE #########################

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        data = account_registration.objects.filter(username=username)
        data1 = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()
        #data2 = account_registration.objects.filter(username=check_username).values_list('account_complete', flat=True).first()

        print("data1" , data)
        print(data1)
        #print(data2)
        if user is not None:

            if data1 == 'Applicant Level 1':
                login(request, user)
                context = {'info': data}
                return render(request, 'html_files/Finish-Registration.html', context)
            
            elif data1 == 'Applicant Level 2':
                login(request, user)
                info1 = account_registration.objects.filter(username=username)
                info2 = other_info.objects.filter(username=username)
                info3 = interview.objects.filter(username=username)

                zippedItems = zip(info1, info2, info3)
                context1 = {'info': zippedItems}
                return render(request, 'html_files/User-Profile1.html', context1)
                
            elif data1 == 'Applicant Level 3':
                login(request, user)
                info1 = account_registration.objects.filter(username=username)
                info2 = other_info.objects.filter(username=username)
                info3 = interview.objects.filter(username=username)

                zippedItems = zip(info1, info2, info3)
                context1 = {'info': zippedItems}
                return render(request, 'html_files/User-Profile1.html', context1)

            elif data1 == 'Employee':
                login(request, user)
                info1 = account_registration.objects.filter(username=username)
                info2 = other_info.objects.filter(username=username)
                info3 = interview.objects.filter(username=username)

                zippedItems = zip(info1, info2, info3)
                context1 = {'info': zippedItems}
                return render(request, 'html_files/User-Profile1.html', context1)

            elif data1 == 'HRManager':
                login(request, user)
                account = account_registration.objects.all()
                user_interview = interview.objects.values('date_time')
                zippedItems = zip(account, user_interview)

                context1 = {'zippedItems': zippedItems}
                return render(request, 'html_files/HRMANAGER.html', context1)
            
            else:
                return redirect('home')
        
        else:
            return redirect('home')
    else:
            return redirect('home')

def signup(request):
    form = first_registration()

    if request.method == "POST":
        form = first_registration(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password_first = form.cleaned_data.get("password1")
            password_confirm = form.cleaned_data.get("password2")

            if password_confirm == password_first:
                position = request.POST.get('job')
                form.instance.account_type = position

                other_info.objects.create(username_id=username)
                interview.objects.create(username_id=username)

                form.save()

                messages.success(request, 'Account successfully created!')
                return redirect('home')

            else:
                messages.warning(request, 'ERROR: Password do not match.')
                return redirect('signup')
   
    context = {'form': form}
    return render(request, 'html_files/Registration-Form.html', context)

def signup1(request, username):  
    form1 = second_registration()

    if request.method == "POST":
        form1 = second_registration(request.POST, request.FILES)

        if form1.is_valid():

            update_birthplace = form1.cleaned_data.get("bplace")
            update_civilstatus = form1.cleaned_data.get("civilstatus")
            update_citizenship = form1.cleaned_data.get("citizenship")
            update_religion = form1.cleaned_data.get("religion")
            update_e_contact = form1.cleaned_data.get("e_contact")
            update_e_no = form1.cleaned_data.get("e_no")
            update_elementary = form1.cleaned_data.get("elementary")
            update_elementary_grad = form1.cleaned_data.get("elementary_grad")
            update_highschool = form1.cleaned_data.get("highschool")
            update_highschool_grad = form1.cleaned_data.get("highschool_grad")
            update_college = form1.cleaned_data.get("college")
            update_college_grad = form1.cleaned_data.get("college_grad")
            update_company1 = form1.cleaned_data.get("company1")
            update_position1 = form1.cleaned_data.get("position1")
            update_from1 = form1.cleaned_data.get("from1")
            update_to1 = form1.cleaned_data.get("to1")
            update_company2 = form1.cleaned_data.get("company2")
            update_position2 = form1.cleaned_data.get("position2")
            update_from2 = form1.cleaned_data.get("from2")
            update_to2 = form1.cleaned_data.get("to2")
            update_ref1 = form1.cleaned_data.get("ref1")
            update_refcon1 = form1.cleaned_data.get("refcon1")
            update_refpos1 = form1.cleaned_data.get("refpos1")
            update_refcom1 = form1.cleaned_data.get("refcom1")
            update_ref2 = form1.cleaned_data.get("ref2")
            update_refcon2 = form1.cleaned_data.get("refcon2")
            update_refpos2 = form1.cleaned_data.get("refpos2")
            update_refcom2 = form1.cleaned_data.get("refcom2")
            update_philhealth = form1.cleaned_data.get("philhealth")
            update_pagibig = form1.cleaned_data.get("pagibig")
            update_TIN = form1.cleaned_data.get("TIN")
            update_NBI = form1.cleaned_data.get("NBI")
            update_SSS = form1.cleaned_data.get("SSS")
            update_med_record = form1.cleaned_data.get("med_record")
            update_signature = form1.cleaned_data.get("bplsignaturece")

            other_info.objects.filter(username=username).update(bplace=update_birthplace, civilstatus=update_civilstatus, citizenship=update_citizenship, religion=update_religion, e_contact=update_e_contact, e_no=update_e_no,
                                                            elementary=update_elementary, elementary_grad=update_elementary_grad, highschool=update_highschool, highschool_grad=update_highschool_grad, college=update_college, college_grad=update_college_grad,
                                                            company1=update_company1, position1=update_position1, from1=update_from1, to1=update_to1, company2=update_company2, position2=update_position2, from2=update_from2, to2=update_to2, ref1=update_ref1,
                                                            refcon1=update_refcon1, refpos1=update_refpos1, refcom1=update_refcom1, ref2=update_ref2, refcon2=update_refcon2, refpos2=update_refpos2, refcom2=update_refcom2, philhealth=update_philhealth, pagibig=update_pagibig,
                                                            TIN=update_TIN, NBI=update_NBI, SSS=update_SSS, med_record=update_med_record, signature=update_signature)

            #other_info.objects.filter(username_id=username).update(form1.save())
    
            account_registration.objects.filter(username=username).update(account_type='Applicant Level 2')
            info1 = account_registration.objects.filter(username=username)
            info2 = other_info.objects.filter(username=username)
            info3 = interview.objects.filter(username=username)

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1.html', context1)

        else:
            return redirect('signup1')
        
    context = {'form': form1}
    return render(request, 'html_files/Registration-Form-Part-2.html', context)

def requirements_satisfied(request, username_id):
    
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

        zippedItems = zip(info1, info2, info3)
        context1 = {'info': zippedItems}
        return render(request, 'html_files/User-Profile1.html', context1)
            


def sort_list(request):
    if request.method == "POST" and "Name" in request.POST:
        
        account = account_registration.objects.order_by('first_name')
        user_interview = interview.objects.order_by('first_name')
        zippedItems = zip(account, user_interview)

        context1 = {'zippedItems': zippedItems}
        return render(request, 'html_files/HRMANAGER.html', context1)

def manage_account(request, username):
    user_account = account_registration.objects.filter(username=username)
    data1 = account_registration.objects.filter(username=username).values_list('account_type', flat=True).first()

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

def complete_info(request):
    return render(request, 'html_files/Finish-Registration.html')


def set_interview(request, username_id):

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

def change_employment(request, username):

    if request.method == "POST" and "Full Time" in request.POST:
        account_registration.objects.filter(username=username).update(employment_status="Full Time Worker")
        messages.success(request, 'Employment was updated on account: ' + username)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Part Time" in request.POST:
        account_registration.objects.filter(username=username).update(employment_status="Part Time Worker")
        messages.success(request, 'Employment was updated on account: ' + username)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "On Leave" in request.POST:
        account_registration.objects.filter(username=username).update(employment_status="On Vacation")
        messages.success(request, 'Employment was updated on account: ' + username)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Resigned" in request.POST:
        account_registration.objects.filter(username=username).update(employment_status="Resigned")
        messages.success(request, 'Employment was updated on account: ' + username)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Fired" in request.POST:
        account_registration.objects.filter(username=username).update(employment_status="Fired")
        messages.success(request, 'Employment was updated on account: ' + username)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    elif request.method == "POST" and "Retired" in request.POST:
        account_registration.objects.filter(username=username).update(employment_status="Retired")
        messages.success(request, 'Employment was updated on account: ' + username)
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)

    else:
        return redirect('change_employment')

def applicant_hired_reject(request, username):
    if request.method == "POST" and "Hire" in request.POST:
        account_registration.objects.filter(username=username).update(account_type="Employee")
        messages.success(request, 'Applicant Successfully Hired!')
        account = account_registration.objects.all()
        context = {'account': account}
        return render(request, 'html_files/HRMANAGER.html', context)


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

            zippedItems = zip(info1, info2, info3)
            context1 = {'info': zippedItems}
            return render(request, 'html_files/User-Profile1.html', context1)

        else:
            return redirect('change_password', username=username)

    context = {'form': form }
    return render(request, 'html_files/Changepassword.html', context)

################################### REDIRECTS ############################################

def home(request):
    data = job_listing.objects.all()
    context = {'job': data}
    return render(request, 'html_files/HOMEWEBSITE.html', context)

def hrdashboard(request):
    account = account_registration.objects.all()
    context = {'account': account}
    return render(request, 'html_files/HRMANAGER.html', context)

def user_profile(request, username):
    info1 = account_registration.objects.filter(username=username)
    info2 = other_info.objects.filter(username_id=username)
    info3 = interview.objects.filter(username_id=username)

    zippedItems = zip(info1, info2, info3)
    context1 = {'info': zippedItems}
    return render(request, 'html_files/User-Profile1.html', context1)

def returntoprofile(request, username):
    info1 = account_registration.objects.filter(username=username)
    info2 = other_info.objects.filter(username_id=username)
    info3 = interview.objects.filter(username_id=username)

    zippedItems = zip(info1, info2, info3)
    context1 = {'info': zippedItems}
    return render(request, 'html_files/User-Profile1.html', context1)

def requirements(request, username):
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

def logout_user(request):
    logout(request)
    return redirect('home')

################################### INACTIVE ############################################


def delete(request):
    return render(request, 'html_files/delete.html')

def addjob(request):
    return render(request, 'html_files/Making-a-Job-Posting.html')

def delete_acc(request):
    return render(request, 'html_files/HRMANAGER.html')

def delete_jobs(request):
    return render(request, 'html_files/HRMANAGER.html')



################################### DEBUG ############################################


