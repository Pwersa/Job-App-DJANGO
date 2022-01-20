from django.shortcuts import render
from django.http import HttpResponse

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

# wassup
