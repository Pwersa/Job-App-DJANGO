from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class first_registration(ModelForm):

    class Meta:
        model = account_registration 
        #fields = ['email', 'password1', 'password2', 'photo', 'first_name', 'middle_name', 'last_name', 'address', 'cellphone', 'birthday']
        fields = '__all__' 

        widgets = {'password1': forms.PasswordInput(), 'password2': forms.PasswordInput()}
        labels = {'email': 'Email (This Will Be Your Login)',
                'password1': 'Password',
                'password2': 'Confirm your Password',
                'photo': 'Upload 1x1 Photo',
                'last_name': 'Surname',
                'first_name': 'First Name',
                'middle_name': 'Middle Name',
                'address': 'Address',
                'cellphone': 'Cellphone Number',
                'birthday': 'Birthday',
                'applyingfor': 'Applying For:'
                }

class second_registration(ModelForm):
    class Meta:
        model = other_info
        #fields = ['bplace']
        fields = '__all__'
        labels = {'bplace': 'Birthplace',
                'civilstatus': 'Civil Status',
                'citizenship': 'Citizenship',
                'religion': 'Religion',
                'e_contact':'Emergency Contact Person',
                'e_no':'Emergency Contact #',
                'elementary':'Elementary School',
                'elementary_grad':'Year Graduated',
                'highschool':'High School',
                'highschool_grad':'Year Graduated',
                'college':'College',
                'college_grad':'Year Graduated',
                'company1':'Company name',
                'position1':'Position in the Company',
                'from1':'Starting date',
                'to1':'Date leaved',
                'company2':'Company name',
                'position2':'Position in the Company',
                'from2':'Starting date',
                'to2':'Date leaved',
                'ref1':'Reference Person',
                'refcon1':'Contact #',
                'refpos1':'Person Position',
                'refcom1':'Rerefence Company',
                'ref2':'Reference Person',
                'refcon2':'Contact #',
                'refpos2':'Person Position',
                'refcom2':'Rerefence Company',
                'philhealth':'Philhealth ID',
                'pagibig':'Pag-ibig ID',
                'TIN':'Tin Number',
                'NBI':'NBI Clearance',
                'SSS':'SSS ID',
                'med_record':'Medical Record',
                'signature':'Signature (Picture)',
                }
