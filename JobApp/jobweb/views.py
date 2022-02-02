from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import account_data
from .models import job_listing

def home(request):
    return render(request, 'html_files/HOMEWEBSITE.html')

def signup(request):
    return render(request, 'html_files/Registration-Form.html')

def hrdashboard(request):
    return render(request, 'html_files/HRMANAGER.html')

def employee(request):
    return render(request, 'html_files/Employee-Details.html')

def applicant(request):
    return render(request, 'html_files/Applicant-Details.html')

def addjob(request):
    return render(request, 'html_files/Making-a-Job-Posting.html')

def profile(request):
    return render(request, 'html_files/User Profile.html')


def createAccount(request):
    accounts = account_data.objects_create(
        email = request.POST['email'],
        password = request.POST['password'],
        photo = request.POST['photo'],
        fullname = request.POST['full_name'],
        password = request.POST['password'],
        address = request.POST['address'],
        cellphone = request.POST['cellphone'],
        birthday = request.POST['birthday'],
        bplace = request.POST['bplace'],
        civilstatus = request.POST['civilstatus'],
        citizenship = request.POST['citizenship'],
        religion = request.POST['religion'],
        econtact = request.POST['e_contact'],
        eno = request.POST['e_no'],
        elementary = request.POST['elementary'],
        elementarygrad = request.POST['elementary_grad'],
        highschool = request.POST['highschool'],
        highschoolgrad = request.POST['highschool_grad'],
        college = request.POST['college'],
        collegegrad = request.POST['college_grad'],
        company1 = request.POST['company1'],
        position1 = request.POST['position1'],
        from1 = request.POST['from1'],
        to1 = request.POST['to1'],
        company2 = request.POST['company2'],
        position2 = request.POST['position2'],
        from2 = request.POST['from2'],
        to2 = request.POST['to2'],
        philhealth = request.POST['philhealth'],
        pagibig = request.POST['pagibig'],
        TIN = request.POST['TIN'],
        NBI = request.POST['NBI'],
        SSS = request.POST['SSS'],
        medrecord = request.POST['med_record'],
        applyingfor = request.POST['applyingfor'],
        job = request.POST['job'],
        accounttype = request.POST['account_type']
        )
    return render(request,'account_index.html')

def showAccount(request):
    accounts = account_data.objects.all()
    context ={'accounts':accounts}
    return render(request,"account_show.html", context)

def createJobs(request):
    joblist = job_listing.objects_create(
        jobtitle = request.Post['jobtitle'],
        jdesc = request.Post['jdesc'],
        nodipl = request.Post['no_dipl'],
        hsgrad = request.Post['hs_grad'],
        colgrad = request.Post['col_grad'],
        nochar = request.Post['no_char'],
        charref1 = request.Post['char_ref1'],
        charref2 = request.Post['char_ref2'],
        salary = request.Post['salary'],
        )
    return render(request,'jobs_index.html')

def showJobs(request):
    joblist = job_listing.objects.all()
    context ={'joblist':joblist}
    return render(request,"jobs_show.html", context)