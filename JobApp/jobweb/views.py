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
    accounts = account_data.objects.create(
        email = request.POST['email'],
        password = request.POST['password'],
        photo = request.POST['photo'],
        #surname = request.POST['full_name'],
        #firstname = request.POST['full_name'],
        #middlename = request.POST['full_name'],
        address = request.POST['address'],
        cellphone = request.POST['cellphone'],
        birthday = request.POST['birthday'],
        bplace = request.POST['bplace'],
        civilstatus = request.POST['civilstatus'],
        citizenship = request.POST['citizenship'],
        religion = request.POST['religion'],
        e_contact = request.POST['emer_cont'],
        e_no = request.POST['emer_contno'],
        elementary = request.POST['elementary'],
        elementary_grad = request.POST['elementary_grad'],
        highschool = request.POST['highschool'],
        highschool_grad = request.POST['highschool_grad'],
        college = request.POST['college'],
        college_grad = request.POST['college_grad'],
        company1 = request.POST['company1'],
        position1 = request.POST['position1'],
        from1 = request.POST['from1'],
        to1 = request.POST['to1'],
        company2 = request.POST['company2'],
        position2 = request.POST['position2'],
        from2 = request.POST['from2'],
        to2 = request.POST['to2'],
        ref1 = request.POST['ref1'],
        refcon1 = request.POST['refcon1'],
        refpos1 = request.POST['refpos1'],
        refcom1 = request.POST['refcom1'],
        ref2 = request.POST['ref2'],
        refcon2 = request.POST['refcon2'],
        refpos2 = request.POST['refpos2'],
        refcom2 = request.POST['refcom2'],
        SSS = request.POST['S_S_S'],
        philhealth = request.POST['philhealth'],
        pagibig = request.POST['pag-ibig'],
        TIN = request.POST['T_I_N'],
        med_record = request.POST['med_record'],
        NBI = request.POST['N_B_I'],
        signature = request.POST['signature'],
        applyingfor = request.POST['applyingfor'],
        #job = request.POST['job'],
        #accounttype = request.POST['account_type'],
        )
    #accounts.save()
    print(accounts)
    return render(request,'html_files/Registration-Form.html')

    

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