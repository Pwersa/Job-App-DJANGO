from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ModelChoiceField
from .models import *

class first_registration(UserCreationForm):
    applyingfor = ModelChoiceField(queryset=job_listing.objects.values_list('jtitle', flat=True))

    class Meta:
        model = account_registration 
        fields = ['username', 'password1', 'password2', 'photo', 'first_name', 'middle_name', 'last_name', 'address', 'cellphone', 'birthday',
                'applyingfor', 'job', 'employment_status', 'account_type']
        #fields = '__all__' 

        widgets = {'password': forms.PasswordInput(), 'password1': forms.PasswordInput()}
        labels = {'username': 'Email (This Will Be Your Username for Login)',
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
        fields = ['bplace', 'civilstatus', 'citizenship', 'religion', 'e_contact', 'e_no', 'elementary', 'elementary_grad', 'highschool', 'highschool_grad', 'college', 'college_grad', 
                'company1', 'position1', 'from1', 'to1', 'company2', 'position2', 'from2', 'to2', 'ref1', 'refcon1', 'refpos1', 'refcom1', 'ref2', 'refcon2', 'refpos2', 'refcom2', 'philhealth', 'pagibig', 
                'TIN', 'NBI', 'SSS', 'med_record', 'signature', ]
        #fields = '__all__'
        labels = {'bplace': 'Birthplace',
                'civilstatus': 'Civil Status',
                'citizenship': 'Citizenship',
                'religion': 'Religion',
                'e_contact':'Emergency Contact Person',
                'e_no':'Emergency Contact No.',
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
                'NBI':'NBI Clearance (To be filled out later, best when record is new.)',
                'SSS':'SSS ID',
                'med_record':'Medical Record (To be filled out later, best when record is new.)',
                'signature':'Signature (Picture)',
                }

class update_password(UserCreationForm):

    class Meta:
        model = account_registration 
        fields = [ 'password1', 'password2']
        #fields = '__all__'